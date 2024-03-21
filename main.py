import pandas as pd
import streamlit as st
import numpy as np
from datetime import datetime, timedelta
from streamlit_tree_select import tree_select
# import sqlalchemy as sa
import altair as alt
from streamlit_date_picker import date_range_picker, PickerType, Unit, date_picker
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
import boto3
from boto3.dynamodb.conditions import Key, Attr
# from pages import chat


def main():
    st.set_page_config(
        page_title="H2 Data Center",  # String or None. Strings get appended with "• Streamlit".
        layout="wide",
        page_icon="💧",  # Can be "centered" or "wide". In the future also "dashboard", etc.
        # initial_sidebar_state="auto",  # Can be "auto", "expanded", "collapsed"
        # page_icon=None,  # String, anything supported by st.image, or None.
    )
    st.markdown(
        """
        <style>
            .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                }
            .sidebar .sidebar-content {
            background-image: linear-gradient(#2e7bcf,#2e7bcf);
            color: white;
            }              
            .css-1aumxhk {
            background-color: #011839;
            background-image: none;
            color: #ffffff
            }
            section[data-testid="stSidebar"] {
                width: 420px !important; # Set the width to your desired value
                background-color: white;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    def init_connection():
        dynamodb = boto3.resource(
            'dynamodb',
            aws_access_key_id = st.secrets['aws_access_key_id'],
            aws_secret_access_key = st.secrets['aws_secret_access_key'],
            region_name = 'us-east-1')
        table = dynamodb.Table('OPC_DB')
        return table

    table = init_connection()

    hrs=pd.read_csv('./streamlit/data/hrs.csv',header=None)
    # hrs = pd.read_csv(r"C:\Users\Administrator\Desktop\hrs.csv", header=None)
    hrs.columns = ['Location', 'Address']

    # @st.cache_data(ttl=3600)
    # def streamlit_init(hrs):
    #     query = "SELECT [Tag] FROM [hmcportal].[dbo].[A_OPC_History] where Time > dateadd(HOUR,-1,Getdate()) and Tag like '%온도%'"
    #     x = pd.read_sql(query, engine)
    #     y = x['Tag'].str.extract(r'(\w+)-.+')
    #     y = y[0].drop_duplicates().reset_index(drop=True)

    #     for idx, i in enumerate(hrs['Location']):
    #         if i in y.to_list():
    #             hrs.loc[idx, 'Connection'] = "Connected"
    #         else:
    #             hrs.loc[idx, 'Connection'] = "Disconnected"
    #     return hrs

    # @st.cache_data(ttl=36000)
    # def stat_query():
    #     query = "SELECT CONVERT(VARCHAR, Date, 23) as Date, Location, data_count from DataCount"
    #     return pd.read_sql(query, engine)

    @st.cache_data(ttl=36000)
    def statistic_query():
        # query = "SELECT [Time] ,[Tag] ,[Value] FROM [hmcportal].[dbo].[A_OPC_Statistic]"
        # return pd.read_sql(query, engine).sort_values(['Tag', 'Time'])
        response = table.query(
            KeyConditionExpression=Key('pk').eq('Statistic')
        )
        x = pd.json_normalize(response['Items'])
        return x[['Time','payload.Tag','payload.Value']]        

    @st.cache_data(ttl=3600)
    def runqry(date_i, loc_i):
        # query = "SELECT Time, Tag, Value FROM A_OPC_History where Time > '" + date_i.strftime(
        #     "%Y-%m-%d") + " 07:00:00' and Time < '" + \
        #         date_i.strftime("%Y-%m-%d") + " 21:00:00' and tag like '%" + loc_i + "%' order by Time asc;"
        # x = pd.read_sql(query, engine)
        # # x = x[x["TAG"].str.contains(r'(OPC UA.(\w+).2.Tags.\w+.\w+.(\w+)-(\w-\d\w)-(.+))')]

        response = table.query(
            KeyConditionExpression=Key('pk').eq(f'{loc_i}-{date_i.strftime("%y%m%d")}')
        )
        x = pd.json_normalize(response['Items'])
        
        # y = pd.concat([x["Time"], x["Tag"].str.extract(r'(\w+)-(\w+)-(\w-\w+)-(.+)'),
        #                x["Value"]], axis=1)

        y = pd.concat([x["Time"], x["pk"].str.extract(r'(\w+)-.+'), x["payload.Tag"].str.extract(r'(\w+)-(\w-\w+)-(.+)'), x["payload.Value"]], axis=1)
        
        y.columns = ["Time", "Location", "Code", "Serial", "Tag", "Value"]
        x['Legend'] = y['Tag']
        z = y["Tag"]
        z = pd.concat([z, z], axis=1)
        z.drop_duplicates(inplace=True)
        z.columns = ["label", "value"]
        z = z.to_dict('records')

        srl = y['Serial'].drop_duplicates()
        srl_trd = []
        for idx_i, i in enumerate(srl):
            atr = y.loc[y['Serial'] == i, 'Code'].drop_duplicates()
            atr_trd = []
            for idx_j, j in enumerate(atr):
                tag = y.loc[(y['Serial'] == i) & (y['Code'] == j), 'Tag'].drop_duplicates()
                tag_trd = []
                for k in tag:
                    tag_trd.append({'label': k, 'value': j + '-' + i + '-' + k})
                atr_trd.append({'label': j, 'value': j + '-' + i, 'children': tag_trd})
            srl_trd.append({'label': i, 'value': i, 'children': atr_trd})
        root = [{'label': loc_i, 'value': loc_i, 'children': srl_trd}]
        return x, y, root

    if 'key' not in st.session_state:
        st.session_state.key = False
    if 'plot' not in st.session_state:
        st.session_state['plot'] = False
    if 'update_key' not in st.session_state:
        st.session_state['update_key'] = False
    if 'update' not in st.session_state:
        st.session_state['update'] = False
    if 'd_key' not in st.session_state:
        st.session_state['d_key'] = False
    if 'd' not in st.session_state:
        st.session_state['d'] = False

    st.text("")
    st.markdown("<h1 style='text-align: center;"
                " color: #235191; font-size: 24px;'>H<sub style='font-size: 24px;'>2</sub> Monitoring Dashboard</h1>", unsafe_allow_html=True)
    tab_chart, non = st.tabs(["📈 Chart", " "])

    col1, col2 = st.columns(2)
    with col1:
        datastreamtab, salestab, hometab = st.tabs(["📄 Data","💵 Sales", "📋 Board"])

    with datastreamtab:
        datastream = statistic_query()
        datastream = datastream.loc[datastream['Tag'].str.contains('ValueCounts'),:]
        st.session_state['d_key'] = True

        datastream['Time'] = pd.to_datetime(datastream.Time)
        datastream['Month'] = datastream['Time'].dt.strftime("%b")
        datastream['Month_sort'] = datastream['Month'].map({'Dec': 1, 'Jan': 2, 'Feb': 3, 'Mar': 4, 'Apr': 5})
        datastream.sort_values('Month_sort', ascending=True, inplace=True)
        st.session_state['d'] = datastream

        if st.session_state['d_key']:
            scale1 = alt.Scale(
                domain=st.session_state['d']['Month'].unique(),
                range=["#4873a0", "#e91e63", "#b7a166"],
            )
            color1 = alt.Color("Month:N", scale=scale1)
            # st.write(st.session_state['d'].Tag.unique())

            scale2 = alt.Scale(
                domain=st.session_state['d'].Tag.unique(),
                # range=["#3f3f3f", "#7c5cbf", "#a43a7a", "#4873a0", "#e91e63", "#b7a166", "#1b94e9", "#7f76d4",
                #        "#efb21e", "#8fc33e", "#b5621f", "#53a372", "#d1483f", "#33b3c5", "#6d95a4", "#d4a7cf"],
            )
            color2 = alt.Color("Tag:N", scale=scale2)

            click1 = alt.selection_multi(encodings=["y"])
            click2 = alt.selection_multi(encodings=["color"])

            bars1 = (
                alt.Chart()
                .mark_bar()
                .encode(
                    x="sum(Value)",
                    y=alt.Y("Month:N",sort=None),
                    color=alt.condition(click1, alt.value("black"), alt.value("lightgray")),
                )
                .properties(width=500, height=60)
                .add_selection(click1)
                .transform_filter(click2)
            )

            bars2 = (
                alt.Chart()
                .mark_bar()
                .encode(
                    x="Tag:N",
                    y="sum(Value)",
                    color=alt.condition(click2, color2, alt.value("lightgray")),
                )
                .properties(width=500, height=150)
                .add_selection(click2)
                .transform_filter(click1)
            )

            lines = (
                alt.Chart()
                .mark_line()
                .encode(
                    alt.X("Time:T", title="Date"),
                    alt.Y(
                        "Value:Q",
                        title="데이터량",
                    ),
                    color=alt.Color('Tag',legend=None),
                )
                .properties(width=500, height=150)
                .transform_filter(click1)
                .transform_filter(click2)
            )

            chart2 = alt.vconcat(bars1, bars2, lines, data=st.session_state['d'], title=f"Data Amount: ")

            st.altair_chart(chart2, theme="streamlit", use_container_width=True)

    with hometab:
        if st.button(label="Connection Status", use_container_width=True):
            hrs_update = streamlit_init(hrs)
            st.session_state['update_key'] = True
            st.session_state['update'] = hrs_update

        if st.session_state['update_key']:
            hometab.table(st.session_state['update'])

    with salestab:
        x = statistic_query()
        x = x.loc[~x['Tag'].str.contains('ValueCounts'),:]
        loc = x.Tag.str.extract(r'(\w+)-.+').iloc[:, 0].drop_duplicates().reset_index(drop=True)
        t = x.groupby([x.Tag.str.extract(r'(\w+)-.+').iloc[:, 0], x.Time.dt.strftime('%Y-%m-%d')])['Value'].sum()
        SalesTable = pd.DataFrame([])
        for i in range(len(loc)):
            test = t[loc[i]].reset_index()
            test["Tag"] = loc[i]
            SalesTable = pd.concat([SalesTable, test], axis=0)

        SalesTable.Time = pd.to_datetime(SalesTable.Time)

        SalesTable['Month'] = SalesTable['Time'].dt.strftime("%b")
        SalesTable['Month_sort'] = SalesTable['Month'].map({'Dec': 1, 'Jan': 2, 'Feb': 3, 'Mar': 4, 'Apr': 5})
        SalesTable.sort_values('Month_sort',inplace=True,ascending=True)
        st.session_state['SalesTable'] = SalesTable

        scale_sales1 = alt.Scale(
            domain=st.session_state['SalesTable']['Month'].unique(),
            range=["#4873a0", "#e91e63", "#b7a166"],
        )

        scale_sales2 = alt.Scale(
            domain=st.session_state['SalesTable'].Tag.unique(),
            range=["#3f3f3f", "#7c5cbf", "#a43a7a", "#4873a0", "#e91e63", "#b7a166", "#1b94e9", "#7f76d4",
                   "#efb21e", "#8fc33e", "#b5621f", "#53a372", "#d1483f", "#33b3c5", "#6d95a4", "#d4a7cf"],
        )
        color_sales2 = alt.Color("Tag:N", scale=scale_sales2)

        click_sales1 = alt.selection_multi(encodings=["y"])
        click_sales2 = alt.selection_multi(encodings=["color"])

        bars_sales1 = (
            alt.Chart()
            .mark_bar()
            .encode(
                x="sum(Value)",
                y=alt.Y("Month:N",sort=None),
                color=alt.condition(click_sales1, alt.value("black"), alt.value("lightgray")),
            )
            .properties(width=500, height=60)
            .add_selection(click_sales1)
            .transform_filter(click_sales2)
        )

        bars_sales2 = (
            alt.Chart()
            .mark_bar()
            .encode(
                x="sum(Value)",
                y="Tag:N",
                color=alt.condition(click_sales2, color_sales2, alt.value("lightgray")),
            )
            .properties(width=500, height=150)
            .add_selection(click_sales2)
            .transform_filter(click_sales1)
        )

        lines_sales = (
            alt.Chart()
            .mark_line()
            .encode(
                alt.X("Time:T", title="Date"),
                alt.Y(
                    "Value:Q",
                    title="데이터량",
                ),
                color=alt.Color('Tag', legend=None),
            )
            .properties(width=500, height=150)
            .transform_filter(click_sales1)
            .transform_filter(click_sales2)
        )

        chart_sales = alt.vconcat(bars_sales1, bars_sales2, lines_sales, data=st.session_state['SalesTable'], title=f"Sales Amount: ")

        st.altair_chart(chart_sales, theme="streamlit", use_container_width=True)

    with col2:
        opr_table, alm_table = st.tabs(["📊 Operation", "❗ Alarm"])

    with st.sidebar:
                    
        
        c1, c2 = st.sidebar.columns([1,2])
        with c1:
            date_i = st.date_input(label="Datetime",value=datetime.now())
        with c2:
            loc_i = st.selectbox("H2 Refueling Station", list(hrs.iloc[:, 0]), index=2)
        st.session_state.key = True
        st.session_state['plot'] = True

        ct = st.container(height=500)

        if st.session_state.key:
            x, y, root = runqry(date_i, loc_i)
            opr = y[(y["Code"] == 'STS')]
            opr['Value'] = opr['Value'].astype(bool)
            opr.set_index("Time", drop=True, inplace=True)
            alm = y[(y["Code"] == 'ALM')]
            alm['Value'] = alm['Value'].astype(bool)
            alm.set_index("Time", drop=True, inplace=True)
            opr_table.dataframe(opr, height = int(35.2*(19+1)), use_container_width=True)
            alm_table.dataframe(alm, height = int(35.2*(19+1)), use_container_width=True)

        if st.session_state['plot']:
            with ct:
                return_select = tree_select(root,
                                            checked=[root[0]['children'][0]['children'][0]['children'][0]['value']],
                                            expanded=[root[0]['value'], root[0]['children'][0]['value'],
                                                      root[0]['children'][0]['children'][0]['value']])

    
    if st.session_state['plot']:
        if return_select["checked"]:
            y2 = x.loc[x["Tag"].str.contains('|'.join(return_select["checked"]))]
            y2.reset_index(drop=True, inplace=True)
            try:
                ana = y2.loc[y2["Tag"].str.contains('TAG')]
                ana['Time']= ana['Time'].dt.tz_localize('Asia/Seoul')
                ana.reset_index(drop=True, inplace=True)
                dig = y2.loc[y2["Tag"].str.contains('ALM|STS')]
                dig['Time']= dig['Time'].dt.tz_localize('Asia/Seoul')
                dig.reset_index(drop=True, inplace=True)
            except Exception as e:
                st.write(e)
            try:
                line_chart = alt.Chart(ana).mark_line().encode(
                    x='Time:T',
                    y='Value:Q',
                    color='Legend'
                )
                vertical_line = alt.Chart(dig).mark_rule().encode(
                    x='Time:T',
                    color='Legend'
                )
                combined_chart = line_chart + vertical_line
                tab_chart.altair_chart(combined_chart, use_container_width=True)
            except Exception as e:
                st.write(e)
    else:
        data = pd.DataFrame({
            'x': range(10),
            'y': [i ** 2 for i in range(10)]
        })
        base = alt.Chart(data).mark_line().encode(
            x='x',
            y='y'
        )
        tab_chart.altair_chart(base, use_container_width=True)


if __name__ == "__main__":
    main()
