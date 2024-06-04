import streamlit as st

# HTML 코드를 작성합니다.
html_code = """
<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"/><title>CV - Jinwoo Lee</title><style>
/* cspell:disable-file */
/* webkit printing magic: print all background colors */
html {
	-webkit-print-color-adjust: exact;
}
* {
	box-sizing: border-box;
	-webkit-print-color-adjust: exact;
}

html,
body {
	margin: 0;
	padding: 0;
}
@media only screen {
	body {
		margin: 2em auto;
		max-width: 900px;
		color: rgb(55, 53, 47);
	}
}

body {
	line-height: 1.5;
	white-space: pre-wrap;
}

a,
a.visited {
	color: inherit;
	text-decoration: underline;
}

.pdf-relative-link-path {
	font-size: 80%;
	color: #444;
}

h1,
h2,
h3 {
	letter-spacing: -0.01em;
	line-height: 1.2;
	font-weight: 600;
	margin-bottom: 0;
}

.page-title {
	font-size: 2.5rem;
	font-weight: 700;
	margin-top: 0;
	margin-bottom: 0.75em;
}

h1 {
	font-size: 1.875rem;
	margin-top: 1.875rem;
}

h2 {
	font-size: 1.5rem;
	margin-top: 1.5rem;
}

h3 {
	font-size: 1.25rem;
	margin-top: 1.25rem;
}

.source {
	border: 1px solid #ddd;
	border-radius: 3px;
	padding: 1.5em;
	word-break: break-all;
}

.callout {
	border-radius: 3px;
	padding: 1rem;
}

figure {
	margin: 1.25em 0;
	page-break-inside: avoid;
}

figcaption {
	opacity: 0.5;
	font-size: 85%;
	margin-top: 0.5em;
}

mark {
	background-color: transparent;
}

.indented {
	padding-left: 1.5em;
}

hr {
	background: transparent;
	display: block;
	width: 100%;
	height: 1px;
	visibility: visible;
	border: none;
	border-bottom: 1px solid rgba(55, 53, 47, 0.09);
}

img {
	max-width: 100%;
}

@media only print {
	img {
		max-height: 100vh;
		object-fit: contain;
	}
}

@page {
	margin: 1in;
}

.collection-content {
	font-size: 0.875rem;
}

.column-list {
	display: flex;
	justify-content: space-between;
}

.column {
	padding: 0 1em;
}

.column:first-child {
	padding-left: 0;
}

.column:last-child {
	padding-right: 0;
}

.table_of_contents-item {
	display: block;
	font-size: 0.875rem;
	line-height: 1.3;
	padding: 0.125rem;
}

.table_of_contents-indent-1 {
	margin-left: 1.5rem;
}

.table_of_contents-indent-2 {
	margin-left: 3rem;
}

.table_of_contents-indent-3 {
	margin-left: 4.5rem;
}

.table_of_contents-link {
	text-decoration: none;
	opacity: 0.7;
	border-bottom: 1px solid rgba(55, 53, 47, 0.18);
}

table,
th,
td {
	border: 1px solid rgba(55, 53, 47, 0.09);
	border-collapse: collapse;
}

table {
	border-left: none;
	border-right: none;
}

th,
td {
	font-weight: normal;
	padding: 0.25em 0.5em;
	line-height: 1.5;
	min-height: 1.5em;
	text-align: left;
}

th {
	color: rgba(55, 53, 47, 0.6);
}

ol,
ul {
	margin: 0;
	margin-block-start: 0.6em;
	margin-block-end: 0.6em;
}

li > ol:first-child,
li > ul:first-child {
	margin-block-start: 0.6em;
}

ul > li {
	list-style: disc;
}

ul.to-do-list {
	padding-inline-start: 0;
}

ul.to-do-list > li {
	list-style: none;
}

.to-do-children-checked {
	text-decoration: line-through;
	opacity: 0.375;
}

ul.toggle > li {
	list-style: none;
}

ul {
	padding-inline-start: 1.7em;
}

ul > li {
	padding-left: 0.1em;
}

ol {
	padding-inline-start: 1.6em;
}

ol > li {
	padding-left: 0.2em;
}

.mono ol {
	padding-inline-start: 2em;
}

.mono ol > li {
	text-indent: -0.4em;
}

.toggle {
	padding-inline-start: 0em;
	list-style-type: none;
}

/* Indent toggle children */
.toggle > li > details {
	padding-left: 1.7em;
}

.toggle > li > details > summary {
	margin-left: -1.1em;
}

.selected-value {
	display: inline-block;
	padding: 0 0.5em;
	background: rgba(206, 205, 202, 0.5);
	border-radius: 3px;
	margin-right: 0.5em;
	margin-top: 0.3em;
	margin-bottom: 0.3em;
	white-space: nowrap;
}

.collection-title {
	display: inline-block;
	margin-right: 1em;
}

.page-description {
    margin-bottom: 2em;
}

.simple-table {
	margin-top: 1em;
	font-size: 0.875rem;
	empty-cells: show;
}
.simple-table td {
	height: 29px;
	min-width: 120px;
}

.simple-table th {
	height: 29px;
	min-width: 120px;
}

.simple-table-header-color {
	background: rgb(247, 246, 243);
	color: black;
}
.simple-table-header {
	font-weight: 500;
}

time {
	opacity: 0.5;
}

.icon {
	display: inline-block;
	max-width: 1.2em;
	max-height: 1.2em;
	text-decoration: none;
	vertical-align: text-bottom;
	margin-right: 0.5em;
}

img.icon {
	border-radius: 3px;
}

.user-icon {
	width: 1.5em;
	height: 1.5em;
	border-radius: 100%;
	margin-right: 0.5rem;
}

.user-icon-inner {
	font-size: 0.8em;
}

.text-icon {
	border: 1px solid #000;
	text-align: center;
}

.page-cover-image {
	display: block;
	object-fit: cover;
	width: 100%;
	max-height: 30vh;
}

.page-header-icon {
	font-size: 3rem;
	margin-bottom: 1rem;
}

.page-header-icon-with-cover {
	margin-top: -0.72em;
	margin-left: 0.07em;
}

.page-header-icon img {
	border-radius: 3px;
}

.link-to-page {
	margin: 1em 0;
	padding: 0;
	border: none;
	font-weight: 500;
}

p > .user {
	opacity: 0.5;
}

td > .user,
td > time {
	white-space: nowrap;
}

input[type="checkbox"] {
	transform: scale(1.5);
	margin-right: 0.6em;
	vertical-align: middle;
}

p {
	margin-top: 0.5em;
	margin-bottom: 0.5em;
}

.image {
	border: none;
	margin: 1.5em 0;
	padding: 0;
	border-radius: 0;
	text-align: center;
}

.code,
code {
	background: rgba(135, 131, 120, 0.15);
	border-radius: 3px;
	padding: 0.2em 0.4em;
	border-radius: 3px;
	font-size: 85%;
	tab-size: 2;
}

code {
	color: #eb5757;
}

.code {
	padding: 1.5em 1em;
}

.code-wrap {
	white-space: pre-wrap;
	word-break: break-all;
}

.code > code {
	background: none;
	padding: 0;
	font-size: 100%;
	color: inherit;
}

blockquote {
	font-size: 1.25em;
	margin: 1em 0;
	padding-left: 1em;
	border-left: 3px solid rgb(55, 53, 47);
}

.bookmark {
	text-decoration: none;
	max-height: 8em;
	padding: 0;
	display: flex;
	width: 100%;
	align-items: stretch;
}

.bookmark-title {
	font-size: 0.85em;
	overflow: hidden;
	text-overflow: ellipsis;
	height: 1.75em;
	white-space: nowrap;
}

.bookmark-text {
	display: flex;
	flex-direction: column;
}

.bookmark-info {
	flex: 4 1 180px;
	padding: 12px 14px 14px;
	display: flex;
	flex-direction: column;
	justify-content: space-between;
}

.bookmark-image {
	width: 33%;
	flex: 1 1 180px;
	display: block;
	position: relative;
	object-fit: cover;
	border-radius: 1px;
}

.bookmark-description {
	color: rgba(55, 53, 47, 0.6);
	font-size: 0.75em;
	overflow: hidden;
	max-height: 4.5em;
	word-break: break-word;
}

.bookmark-href {
	font-size: 0.75em;
	margin-top: 0.25em;
}

.sans { font-family: ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol"; }
.code { font-family: "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace; }
.serif { font-family: Lyon-Text, Georgia, ui-serif, serif; }
.mono { font-family: iawriter-mono, Nitti, Menlo, Courier, monospace; }
.pdf .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK JP'; }
.pdf:lang(zh-CN) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK SC'; }
.pdf:lang(zh-TW) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK TC'; }
.pdf:lang(ko-KR) .sans { font-family: Inter, ui-sans-serif, -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, "Apple Color Emoji", Arial, sans-serif, "Segoe UI Emoji", "Segoe UI Symbol", 'Twemoji', 'Noto Color Emoji', 'Noto Sans CJK KR'; }
.pdf .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .code { font-family: Source Code Pro, "SFMono-Regular", Menlo, Consolas, "PT Mono", "Liberation Mono", Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.pdf .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK JP'; }
.pdf:lang(zh-CN) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK SC'; }
.pdf:lang(zh-TW) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK TC'; }
.pdf:lang(ko-KR) .serif { font-family: PT Serif, Lyon-Text, Georgia, ui-serif, serif, 'Twemoji', 'Noto Color Emoji', 'Noto Serif CJK KR'; }
.pdf .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK JP'; }
.pdf:lang(zh-CN) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK SC'; }
.pdf:lang(zh-TW) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK TC'; }
.pdf:lang(ko-KR) .mono { font-family: PT Mono, iawriter-mono, Nitti, Menlo, Courier, monospace, 'Twemoji', 'Noto Color Emoji', 'Noto Sans Mono CJK KR'; }
.highlight-default {
	color: rgba(55, 53, 47, 1);
}
.highlight-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.highlight-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.highlight-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.highlight-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.highlight-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.highlight-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.highlight-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.highlight-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.highlight-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.highlight-gray_background {
	background: rgba(241, 241, 239, 1);
}
.highlight-brown_background {
	background: rgba(244, 238, 238, 1);
}
.highlight-orange_background {
	background: rgba(251, 236, 221, 1);
}
.highlight-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.highlight-teal_background {
	background: rgba(237, 243, 236, 1);
}
.highlight-blue_background {
	background: rgba(231, 243, 248, 1);
}
.highlight-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.highlight-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.highlight-red_background {
	background: rgba(253, 235, 236, 1);
}
.block-color-default {
	color: inherit;
	fill: inherit;
}
.block-color-gray {
	color: rgba(120, 119, 116, 1);
	fill: rgba(120, 119, 116, 1);
}
.block-color-brown {
	color: rgba(159, 107, 83, 1);
	fill: rgba(159, 107, 83, 1);
}
.block-color-orange {
	color: rgba(217, 115, 13, 1);
	fill: rgba(217, 115, 13, 1);
}
.block-color-yellow {
	color: rgba(203, 145, 47, 1);
	fill: rgba(203, 145, 47, 1);
}
.block-color-teal {
	color: rgba(68, 131, 97, 1);
	fill: rgba(68, 131, 97, 1);
}
.block-color-blue {
	color: rgba(51, 126, 169, 1);
	fill: rgba(51, 126, 169, 1);
}
.block-color-purple {
	color: rgba(144, 101, 176, 1);
	fill: rgba(144, 101, 176, 1);
}
.block-color-pink {
	color: rgba(193, 76, 138, 1);
	fill: rgba(193, 76, 138, 1);
}
.block-color-red {
	color: rgba(212, 76, 71, 1);
	fill: rgba(212, 76, 71, 1);
}
.block-color-gray_background {
	background: rgba(241, 241, 239, 1);
}
.block-color-brown_background {
	background: rgba(244, 238, 238, 1);
}
.block-color-orange_background {
	background: rgba(251, 236, 221, 1);
}
.block-color-yellow_background {
	background: rgba(251, 243, 219, 1);
}
.block-color-teal_background {
	background: rgba(237, 243, 236, 1);
}
.block-color-blue_background {
	background: rgba(231, 243, 248, 1);
}
.block-color-purple_background {
	background: rgba(244, 240, 247, 0.8);
}
.block-color-pink_background {
	background: rgba(249, 238, 243, 0.8);
}
.block-color-red_background {
	background: rgba(253, 235, 236, 1);
}
.select-value-color-uiBlue { background-color: rgba(35, 131, 226, .07); }
.select-value-color-pink { background-color: rgba(245, 224, 233, 1); }
.select-value-color-purple { background-color: rgba(232, 222, 238, 1); }
.select-value-color-green { background-color: rgba(219, 237, 219, 1); }
.select-value-color-gray { background-color: rgba(227, 226, 224, 1); }
.select-value-color-transparentGray { background-color: rgba(227, 226, 224, 0); }
.select-value-color-translucentGray { background-color: rgba(255, 255, 255, 0.0375); }
.select-value-color-orange { background-color: rgba(250, 222, 201, 1); }
.select-value-color-brown { background-color: rgba(238, 224, 218, 1); }
.select-value-color-red { background-color: rgba(255, 226, 221, 1); }
.select-value-color-yellow { background-color: rgba(253, 236, 200, 1); }
.select-value-color-blue { background-color: rgba(211, 229, 239, 1); }
.select-value-color-pageGlass { background-color: undefined; }
.select-value-color-washGlass { background-color: undefined; }

.checkbox {
	display: inline-flex;
	vertical-align: text-bottom;
	width: 16;
	height: 16;
	background-size: 16px;
	margin-left: 2px;
	margin-right: 5px;
}

.checkbox-on {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20width%3D%2216%22%20height%3D%2216%22%20fill%3D%22%2358A9D7%22%2F%3E%0A%3Cpath%20d%3D%22M6.71429%2012.2852L14%204.9995L12.7143%203.71436L6.71429%209.71378L3.28571%206.2831L2%207.57092L6.71429%2012.2852Z%22%20fill%3D%22white%22%2F%3E%0A%3C%2Fsvg%3E");
}

.checkbox-off {
	background-image: url("data:image/svg+xml;charset=UTF-8,%3Csvg%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2016%2016%22%20fill%3D%22none%22%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%3E%0A%3Crect%20x%3D%220.75%22%20y%3D%220.75%22%20width%3D%2214.5%22%20height%3D%2214.5%22%20fill%3D%22white%22%20stroke%3D%22%2336352F%22%20stroke-width%3D%221.5%22%2F%3E%0A%3C%2Fsvg%3E");
}
	
</style></head><body><article id="12269f3b-13ea-4c48-9998-b5d534218645" class="page sans"><header><h1 class="page-title">CV - Jinwoo Lee</h1><p class="page-description"></p></header><div class="page-body"><h3 id="fe90909f-80d2-407d-bb12-97a5a53c41b1" class="">Education</h3><hr id="d8aaeeea-ceed-4dee-8590-48d1a1ee68da"/><div id="57310c1d-92fc-4e63-8f43-234eefa9bf26" class="column-list"><div id="12819f46-bd40-43a1-9fd7-f04401972e04" style="width:29.166666666666664%" class="column"><p id="f5e78457-cf5a-4d56-9fe0-89255fe82b28" class="">Mar. 2011 ~<br/>Aug. 2017<br/></p></div><div id="07fcc41d-05df-4f7c-b43a-1f02dcc1b38f" style="width:83.33333333333333%" class="column"><p id="a0335de2-e021-4350-9882-8a9ed4955c7c" class=""><strong>Hanyang University</strong><br/>Division of Mechanical Engineering<br/>Thesis: AR계수 및 은닉마르코프 모델을 활용한 용접 결함 검출 방법<br/>Advisor: Sehun Rhee<br/>Mechanical Engineering<br/></p></div><div id="9a88f61c-75a0-4f56-94d6-27fad2b563e1" style="width:29.166666666666696%" class="column"><p id="d113270e-4411-4328-992f-58e8d1c7bc99" class="">Seoul,<br/>Korea<br/></p></div></div><h3 id="7a6cb971-f2fd-4909-917b-3de141779e71" class="">Career</h3><hr id="7c1e9d56-a5ca-41a4-853b-00cfef03212c"/><div id="4305523d-73e0-4295-8e60-692d2125a031" class="column-list"><div id="6a6d1d37-0002-44af-a4d4-d2af276edbc2" style="width:37.5%" class="column"><p id="3fe67c6c-e1c8-4d27-a8a7-d4bb82943110" class="">Dec. 2018 ~<br/>Present<br/></p></div><div id="edac7a3c-cfb8-4528-a88c-9ece388c194e" style="width:108.33333333333334%" class="column"><p id="7d426cb3-b872-4f0e-b243-1689ca1c7cee" class="">한국가스기술공사(Korea Gas Technology Corporation)</p><p id="d3b80fc3-da0a-49d4-94be-2c2092910286" class="">직책: 선임연구원</p><p id="293d9141-ea87-43f6-95f3-461ad8e57e32" class="">소속 부서: 에너지사업개발처 신에너지연구원<br/>수행 업무: 데이터-모델 기반 엔지니어링 및 설비건전성관리(PHM) 연구 수행<br/></p></div><div id="28cbc292-f951-4fd2-8b37-0868f32ec0c6" style="width:41.6666666666667%" class="column"><p id="ffdce0ec-28c0-4844-8717-52bd1ae2ef6e" class="">1227, Daedeok-daero, Yuseong-gu, Daejeon, Korea</p><p id="382c8ac1-32ab-4942-b9a4-f6c299be419e" class="">
</p></div></div><h3 id="01afe463-76f7-415f-9be6-88682299b7bc" class="">Projects</h3><hr id="55351070-e7ad-4994-ba5d-5b48ca42e5af"/><ul id="eea21131-dc88-4701-b2b7-efc986a9fb82" class="bulleted-list"><li style="list-style-type:disc"><strong>수소충전소 설계 및 운전 안전성 검증 사전진단 프로그램 개발 (산업부, Apr. 2022 ~ Present)</strong><ul id="a8997b6e-8148-4b2d-9de4-0383319fbf5d" class="bulleted-list"><li style="list-style-type:circle"><em>과제번호: 20227310100060</em></li></ul><ul id="06cc882b-ddac-41ef-acf8-02f5eba85395" class="bulleted-list"><li style="list-style-type:circle">액체 및 기체 수소충전소 해석 모델 개발 - Simulink Simscape</li></ul><ul id="4af7e653-76bf-41d4-8a36-8382ff407979" class="bulleted-list"><li style="list-style-type:circle">수소충전 프로토콜 개발 - Simulink Stateflow</li></ul><ul id="0fa5c2d3-2c8c-43af-bd46-6cd084559175" class="bulleted-list"><li style="list-style-type:circle">수소충전소 위험성 평가 및 사고 시나리오 도출</li></ul></li></ul><ul id="41d0bc9a-9819-4619-8e86-39de80343fab" class="bulleted-list"><li style="list-style-type:disc"><strong>수소충전소 압축기 현장 성능평가 가이드라인 개발(산업부, Apr. 2021 ~ Present)</strong><ul id="36cbd0a5-b53b-47c1-b433-867356f72ddb" class="bulleted-list"><li style="list-style-type:circle"><em>과제번호: 20215810100050</em></li></ul><ul id="48931134-6632-41a1-acef-3e349e21848b" class="bulleted-list"><li style="list-style-type:circle">설비 고장메카니즘 FMEA - FTA 분석</li></ul><ul id="35373b38-ee2c-499c-a3a7-a7fcc2233254" class="bulleted-list"><li style="list-style-type:circle">모델 기반 수소누출 감지 시스템 구축 - Simscape 진단 모델 구축</li></ul><ul id="1fde6374-20c7-454f-b573-0ed0e070d749" class="bulleted-list"><li style="list-style-type:circle">클라우드 기반 실시간 진단 시스템 구축</li></ul></li></ul><ul id="6b2e57b8-ba39-4d5d-a543-9dbbc9f8a344" class="bulleted-list"><li style="list-style-type:disc"><strong>액화수소충전소 공정 최적화 (SK E&amp;S, 연구 용역, Apr. 2024 ~ Present)</strong><ul id="5ac12145-185d-4bad-ac46-059ad00a09b0" class="bulleted-list"><li style="list-style-type:circle">액화수소충전소 BOG 과다 발생 및 냉매 냉각불량 문제 해결방안 제시</li></ul><ul id="671281f9-7574-4c47-a7bc-e5839ce92625" class="bulleted-list"><li style="list-style-type:circle">액화수소충전소 모델 기반 공정 최적화 - Simulink Simscape</li></ul></li></ul><ul id="ac8651c3-e82e-4b27-a510-cfa54328ba78" class="bulleted-list"><li style="list-style-type:disc"><strong>수소통합모니터링시스템 개발 및 고도화(자체 프로젝트, Apr. 2020 ~ Present)</strong><ul id="1ce7773c-650c-4067-ae47-94692cb45312" class="bulleted-list"><li style="list-style-type:circle">설비모니터링 웹 대시보드 구축 - Streamlit</li></ul><ul id="f7ccf784-6c4e-496a-8b42-2246a7654c54" class="bulleted-list"><li style="list-style-type:circle">RCM 기반 설비분류체계 및 PI System 실시간 DB 구축</li></ul><ul id="2cbe5218-fdbd-4204-88c1-19b49c86f518" class="bulleted-list"><li style="list-style-type:circle">생성형 AI 기반 진단 솔루션 개발</li></ul></li></ul><ul id="e2376d69-679c-471a-b64f-07a6cfd90caf" class="bulleted-list"><li style="list-style-type:disc"><strong>액화수소 충전소 구축 연계 안전성 평가/실증 및 안전기준 개발 (산업부, Apr. 2022 ~ Present)</strong><ul id="26da3901-2afd-4eef-944f-9fd4b6492976" class="bulleted-list"><li style="list-style-type:circle"><em>과제번호: 20227310100010</em></li></ul><ul id="5f0edfbc-67da-4cd7-a15f-ef263d6722d1" class="bulleted-list"><li style="list-style-type:circle">액체수소충전소 CAPEX &amp; OPEX 자료 확보 및 경제성 분석</li></ul><ul id="7bad6819-db1d-476c-9ca5-12ffa7a5f345" class="bulleted-list"><li style="list-style-type:circle">액체수소충전소 System Engineering 수행</li></ul></li></ul><ul id="33aa3661-ba18-4eec-8cac-1d09bf2b0350" class="bulleted-list"><li style="list-style-type:disc"><strong>천연가스설비 신뢰성 향상을 위한 Big Data 시스템 개발  (자체 연구과제, Jan. 2019 ~ Mar. 2022)</strong><ul id="4696d3f8-b028-4e55-acaa-14f05d8977b0" class="bulleted-list"><li style="list-style-type:circle">상태이상감지 및 회전기기 열화단계 분류 모델 개발</li></ul><ul id="0a374235-f4e9-47ab-a04b-6566ffee7d84" class="bulleted-list"><li style="list-style-type:circle">원심펌프 임펠러 가공 시 성능변화 예측 모델 개발</li></ul></li></ul><ul id="733f665f-f523-4573-a24e-a5aeecf09722" class="bulleted-list"><li style="list-style-type:disc"><strong>방폭형 수소누출 영상탐지장치 개발 (공동연구과제, 에스엠인스트루먼트, Dec. 2020 ~ Present)</strong><ul id="79dfc327-7ed9-4703-a444-1c59c4ccde49" class="bulleted-list"><li style="list-style-type:circle">수소누출 영상탐지장치의 감도 개선을 위한 알고리즘 고안</li></ul><ul id="1cf84ad6-b748-41fa-831c-bcf58696a086" class="bulleted-list"><li style="list-style-type:circle">객체 인식 모델 개발</li></ul><p id="cdc1025f-4daa-4f9a-b188-94288f756cd8" class="">
</p></li></ul><h3 id="76a66c9d-68a7-46ab-baae-32223f39a640" class="">Publications</h3><hr id="50f910d8-140e-4659-8858-845547aaf466"/><ol type="1" id="f6545255-c826-4407-8e4f-e6296254c704" class="numbered-list" start="1"><li>Ji-Wook Kim, Hong-In Won, Dong-Yong Park, et al. Study on stochastic and autoregressive time series forecasting for hydrogen refueling station. <em>IEEE Access</em>. 2023:141598. doi: 10.1109/ACCESS.2023.3342857.</li></ol><ol type="1" id="488d5738-2889-4393-bf54-47ba7f9c34f0" class="numbered-list" start="2"><li>배성준, 임하늘, 나서연, et al. 수소자동차충전소의 수소압축장치 성능평가를 위한 분류체계 및 rcm 전략수립 연구. <em>한국가스학회지</em>. 2023;27(1):48.</li></ol><ol type="1" id="bd1ccd2f-eb7b-4b3a-a6ab-ac6b8c463853" class="numbered-list" start="3"><li>이아영, 장현준, 이진우, 조원정. 원심펌프 회전차 modification시 성능개선에 관한 유동해석 연구. <em>한국가스학회지</em>. 2020;24(2):1.</li></ol><ol type="1" id="ad8adb71-f9b5-4e1c-9c0a-d56b986e4c44" class="numbered-list" start="4"><li>Jin-Woo Lee, Ji-Wook Kim, Yang-Joong Kwon, et al. Model-Based Method for Leak Detection for Reciprocating Compressor of the Hydrogen Refueling Station . IEEE Transactions on Reliability - Under review</li></ol><p id="a60436b3-30ce-4971-963b-af57dfbd74f5" class="">
</p><h3 id="97a3f9a5-aa3b-4b9d-912c-322d3ba1ad95" class="">Conferences</h3><hr id="d6d91251-b9db-4bc9-a081-ff6d032c6cf6"/><ol type="1" id="b1c69b75-5d02-46cd-aee1-3ba197a33ff1" class="numbered-list" start="1"><li>Lee J, Cho W, Choi J. Fault detection for IoT hydrogen refueling station system using a combined hidden markov model mixed with gaussian. <em>2021 International Conference on Electrical, Computer, Communications and Mechatronics Engineering (ICECCME), Electrical, Computer, Communications and Mechatronics Engineering (ICECCME), 2021 International Conference on</em>. 2021:1. doi: 10.1109/ICECCME52200.2021.9590853.</li></ol><ol type="1" id="64053da2-b7f4-4d56-852a-69cf5ba5312b" class="numbered-list" start="2"><li>이진우 (Jinwoo Lee), 최진혁 (Jinhyuk Choi), 박성수 (Seongsoo Park), 서정수 (Jungsoo Suh). FMECA 및 bayesian network network기법을 활용한 수소충전소 고장진단 방법. <em>대한기계학회 춘추학술대회</em>. 2023;2023(7):23.</li></ol><ol type="1" id="14cc7414-2c96-46aa-a607-f8f97bd1d558" class="numbered-list" start="3"><li>이진우 (Jinwoo Lee), 한종일 (Jongil Han), 서정수 (Jungsoo Suh), 김경덕 (Kyungduk Kim). 모델 기반 수소 충전 프로세스 모니터링 기법 개발. <em>한국가스학회 학술대회논문집</em>. 2023;2023(11):103.</li></ol><ol type="1" id="2064eefc-c23d-4f46-a2e0-2b2ff067736a" class="numbered-list" start="4"><li>이진우 (Jinwoo Lee), 최진혁 (Jinhyuk Choi), 신상봉 (Sangbong Shin), 한종일 (Jongil Han). 수소충전소 디지털 전환을 통한 설비 건전성 관리 및 안전성 사전진단 방법. <em>한국가스학회 학술대회논문집</em>. 2022;2022(11):89.</li></ol><ol type="1" id="29029ebe-1762-4a13-b49f-0904218fcaa7" class="numbered-list" start="5"><li>이진우 (LEE JINWOO), 최진혁 (CHOI JINHYUCK), 신상봉 (SHIN SANGBONG). 수소충전소 설계 및 운전 안전성 검증 사전 진단프로그램 개발. <em>한국가스학회 학술대회논문집</em>. 2022;2022(5):101.</li></ol><ol type="1" id="8800ac6c-d05c-40fb-9795-46927c7ca544" class="numbered-list" start="6"><li>이진우 (Jin-woo Lee), 최진혁 (Jin-Hyuk Choi), 조원정 (Won-Jeong Choi), 나광호 (Gwang-Ho Nah). 은닉마르코프 모델 및 구조학습법을 통한 수소충전소 설비의 베이지안 네트워크 모델 추론. <em>한국가스학회 학술대회논문집</em>. 2021;2021(5):210.</li></ol><ol type="1" id="a4af21d3-c21c-4af2-a472-d591e54cd47e" class="numbered-list" start="7"><li>Choi J, Lee J, Cho WJ. Prognostics by classifying degradation stage on lambda architecture. <em>2020 IEEE International Conference on Prognostics and Health Management (ICPHM), Prognostics and Health Management (ICPHM), 2020 IEEE International Conference on</em>. 2020:1. doi: 10.1109/ICPHM49022.2020.9187061.</li></ol><ol type="1" id="ccb9853c-d597-4f8a-891c-7a3ea23b76c5" class="numbered-list" start="8"><li>최진혁 (Jin-hyuck Choi), 장대식 (Dae-sic Jang), 이진우 (Jin-woo Lee), 조원정 (Won-jung Cho). 천연가스설비 hadoop 기반 예지정비 시스템. <em>한국가스학회 학술대회논문집</em>. 2019;2019(10):123.</li></ol><p id="c7cdf162-ad0b-4334-9e0b-0e74fba628b5" class="">
</p><h3 id="f2f49645-457f-4144-b998-8af3b0caa7b2" class="">Patents</h3><hr id="63d6d715-5fe6-426b-a41d-691c9aa6ecb5"/><ol type="1" id="261fa26f-c384-4a0a-b624-3a07b9cf089d" class="numbered-list" start="1"><li>CHOI JIN HYUCK, CHO WON JEONG, LEE JIN WOO, &quot;Failure diagnostic method based on cluster of fault data&quot;, KR-Registration No. 10-2123522-0000</li></ol><ol type="1" id="cc5f2c04-c34e-4627-bd50-e80104196ba0" class="numbered-list" start="2"><li>CHOI JIN HYUCK, CHO WON JEONG, LEE JIN WOO, NAH KWANG HO, &quot;Method for managing diagnostic data based on conditional probability&quot;, KR-Registration No. 10-2278199-0000</li></ol><ol type="1" id="d12bbf31-c75b-42b8-8d34-edd711a1f0b3" class="numbered-list" start="3"><li>CHOI JIN HYUCK, CHO WON JEONG, LEE JIN WOO, CHOI SO DAM, &quot;Processing method of predictive models for mechanical faults&quot;, KR-Registration No. 10-2249849-0000</li></ol><ol type="1" id="f86978aa-edb4-47fb-9acd-dc8d4bd78b1a" class="numbered-list" start="4"><li>CHO WON JEONG, LEE JIN WOO, &quot;Performance prediction method through shape processing of the outlet of the pump impeller&quot;, KR-Registration No. 10-2426909-0000</li></ol><ol type="1" id="ea7d4ce6-6c8f-4d6d-8487-465b207d6789" class="numbered-list" start="5"><li>YONG GI KIM, IN KWON KIM, WOOK JIN JUNG, JUNG SEOP KIM, KWANG HO NAH, WON JEONG CHO, JIN WOO LEE, &quot;AI Acoustic Image Camera&quot;, KR-Application No. 10-2021-0081491</li></ol><p id="25bcd75a-1006-4435-9aa1-4fd1760de86a" class="">
</p><h3 id="5502c6eb-e062-4034-bda9-9c2dfaf604bc" class="">Skills and Techniques</h3><hr id="1e10a9f2-4c6d-4fbd-85f7-89832153330a"/><ul id="f4016348-9cbf-410a-974c-8b58bd92c651" class="bulleted-list"><li style="list-style-type:disc"><strong>데이터 분석</strong>: Python, MATLAB, R, SQL</li></ul><ul id="e9e3be8f-9467-49f0-8e5e-352081c89f49" class="bulleted-list"><li style="list-style-type:disc"><strong>설계 및 디지털트윈</strong>: Simulink &amp; Simscape, AutoCAD, CATIA, Blender, Unity</li></ul><ul id="6c6678e2-b101-4ba2-8b05-d7e34822926f" class="bulleted-list"><li style="list-style-type:disc"><strong>IoT</strong>: OPC-UA, PI System(OSI Soft), CIMON(PLC &amp; SCADA)</li></ul><ul id="003128ea-f3da-4e08-80f1-7faee8f1838d" class="bulleted-list"><li style="list-style-type:disc"><strong>신뢰성 및 위험성 평가 Tool(RCM, FMEA, HAZOP, LOPA 등)</strong> - exSILentia</li></ul><p id="92d18c0f-b093-40c0-be7e-97d7fa32e839" class="">
</p><h3 id="c11ce333-3815-49c5-acb1-3b7771d8e380" class="">Research</h3><hr id="5af6d0d2-2df3-4546-af5e-1f227b929bad"/><p id="70397944-eac9-40b8-937d-d5047b7318fc" class="">저는 수소산업 설비 엔지니어로서 공정 안전성 검증, 신뢰성 진단, 설계 최적화 분야의 프로젝트를 다수 수행한 경험이 있으며, 위험성 평가, 모델 기반 엔지니어링 및 해석 기술을 통해 다양한 솔루션을 개발하였습니다. 지금까지 수행한 주요 업무와 성과를 다음과 같이 정리해보았습니다.</p><ul id="cb3e9bdf-d3e3-41ff-91de-464f3dd4b025" class="bulleted-list"><li style="list-style-type:disc"><strong>수소통합모니터링 시스템 개발</strong><br/><br/>현직장에서는 수소인프라설비 구축 사업뿐만아니라 지자체로부터 수소충전소나 수소생산기지의 위탁운영사업을 하고 있으며 향후 O&amp;M사업을 위하여 전국에 운영중인 설비에 대해 선제적으로 모니터링과 즉각 대응을 하기위해 수소통합모니터링 시스템을 구축하였습니다. 저는 수소통합모니터링 시스템 개발 담당자로서 네트워크 구축부터 지능형 솔루션 개발까지 역할을 수행하였습니다. 설비의 SCADA와 OPC-UA 통신으로 원격 데이터 피드를 구축하고 설비관리플랫폼인 PI 시스템을 활용하여 설비관리를 위한 시스템을 개발하였습니다. 설비관리 기술의 핵심은 고장 및 정비이력과 운전데이터를 통합하여 관리를 수월하게하고 데이터를 분석하여 진단 및 예측에 활용할 수 있다는 점입니다. 저는 수소충전소 설비를 구조화하여 분류체계를 정의하였고 PI 시스템 태그정보와 설비정보, 알람, 정비이력에 대한 유기적인 데이터관계를 설정하였습니다.<br/><ul id="514eca64-6a8c-4f3f-b44d-7ae543026129" class="bulleted-list"><li style="list-style-type:circle">규칙 기반 전문가 시스템<br/><br/>설비진단시스템을 위한 선행작업으로 RCM기반의 설비별 유지보수전략을 세우고 고장메커니즘 분석을 수행하여 안전성 진단 전문가시스템에 적용할 기준을 개발하였습니다. 우선 설비분류체계를 기준으로 개별 설비마다 고장빈도, 정비 비용 등의 요소를 산출하였으며 이를 종합한 위험도에 따라 사후정비, 예방정비, 상태기반정비, 예측정비 등 유지보수전략을 세웠습니다. 그리고 상태기반정비를 위해 FMEA - FTA 분석을 수행하였고, 이를 통해 도출된 고장물리모델과 유지보수 절차에 따라 고장점검 체크리스크 입력 프로그램을 개발하였습니다. 점검 절차에 따른 체크리스트 입력 모듈을 통해 정비자들이 체계적인 진단과 정비를 수행하여 정형화된 설비이력을 수집할 수 있도록 하였으며, 실시간 데이터 연동을 통해 모니터링 진단과 현장 점검이 복합된 진단 프로세스를 구축하였습니다. 프로젝트를 수행하면서 고장진단 방법에 대한 3건의 특허를 등록하는 성과를 얻었습니다.<br/><figure id="ba65647e-5950-43d9-8d41-2798c444b033" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled.png"><img style="width:768px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled.png"/></a></figure><figure id="f8057cc9-c646-404f-b0c1-883d4f99d913" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%201.png"><img style="width:768px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%201.png"/></a><figcaption>FMEA - FTA 분석을 기반으로 고장점검체크리스트 UI의 모습입니다. </figcaption></figure><figure id="e7339d50-5d98-4212-9523-606b09b2e457" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%202.png"><img style="width:912px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%202.png"/></a></figure><figure id="5d7b1f22-bf45-40aa-9cde-10cd4ab53036" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%203.png"><img style="width:912px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%203.png"/></a></figure></li></ul><p id="311cff71-d590-47d5-8d4e-fa7027f54caf" class="">
</p><ul id="fef4564d-d366-49cf-8968-0f13e16365e6" class="bulleted-list"><li style="list-style-type:circle">머신러닝 모델 기반 이상감지<br/><br/>원격관제시스템을 통해 수집한 설비 데이터를 분석하여 이상상태감지 및 고장진단을 수행하기 위해 머신러닝 및 딥러닝 기법을 활용하여 이상상태감지 프로그램을 개발하였습니다. GMM-HMM 방식, LSTM Auto-Encoder, Isolation-Forest 세가지 기법을 활용하여 이상감지지표를 계산하였으며, 이상상태 감지 시 가장 기여도가 높은 센서나 특징변수를 찾는 방식으로 고장진단 기능을 구현하였습니다. 도출한 이상감지지표와 특징변수는 대시보드에 구현되어 설비관리자로 하여금 설비진단을 수행하는 직관적인 정보를 얻을 수 있습니다. 적용된 기준은 일정기간동안 수소누출 및 기계결함 등의 이상상태에 대해 높은 감지율을 얻을 수 있었고, 관련 내용으로 해외 학술대회 및 MATLAB EXPO에서 발표한 경험이 있습니다.<br/><br/>또한 CHAT-GPT와 같은 생성형 AI를 통해 설비진단 매뉴얼을 제공하는 솔루션에 대해서도 다양한 테스트를하며 가능성을 확인하고 있습니다. 수소인프라설비 운영자들은 설비를 운영하면서 발생하는 설비이력들과, 기술검토서, 유지보수 매뉴얼과 같은 많은 자료들을 빠짐없이 파악하기에 어려움이 있습니다. 따라서 이러한 비정형데이터들을 생성형AI에 학습시켜 이를 기반으로 답변하게하여 도움을 드릴 수 있도록 개발하였습니다. OPENAI에서 제공하는 API를 파이썬 모듈에서 구현하고 Streamlit을 이용하여 웹페이지를 구축하였습니다. 현재 수소충전소 운영자분들이 사용하며 피드백을 주시고 있고, 이를 통해 끊임없이 개선 방안을 모색하고 있습니다.<br/><figure id="44253b01-8eb6-4984-bf24-0c9a6e6fd173" class="image"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%204.png"><img style="width:1008px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%204.png"/></a><figcaption>2023년에 발생한 수소 누출 및 기타 경보에 대해서 가우시안혼합모델 - 은닉마르코프 모델을 활용하여 이상감지를 수행한 모습입니다. 경보가 발생하기 이전에 로그우도가 하락하는 모습을 통해 사전적으로 이상감지 능력이 있음을 검증하였습니다.</figcaption></figure><figure id="8984febd-f7bc-41ff-90aa-a5383846c1f3" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%205.png"><img style="width:864px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%205.png"/></a></figure></li></ul><p id="0ebce03b-6cb5-466c-bd3c-9b11c0ddcf17" class="">
</p><ul id="718aac14-c98d-4178-8bba-8cb33ab89fbd" class="bulleted-list"><li style="list-style-type:circle">3D 정보모델 구축<br/>일반 모니터링 대시보드는 시간에 따른 트렌드를 확인할 수 있지만 공간에 따른 트렌드를 확인하기 위해서는 HMI나 3D 정보모델을 확인하는 것이 좋습니다. 그 중 3D 정보모델은 배관이나 설비의 온도나 압력에 따라 색의 변화로 표현하면서 사용자에게 직관적인 정보를 전달하기 좋습니다. 함덕 그린수소충전소에 3D 정보모델 웹페이지를 시범 적용한 모습이 아래 나와있습니다.<br/>링크: <br/><a href="http://beyond.infoin.biz:60003/"><span style="border-bottom:0.05em solid">http://beyond.infoin.biz:60003/</span></a></li></ul><figure id="ed615672-c273-4fe1-ac72-88c94a6cb65c" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%206.png"><img style="width:960px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%206.png"/></a></figure><p id="125c19a0-0054-41ea-ae72-1402e9175417" class="">
</p></li></ul><ul id="10ca8423-9894-453f-a5b9-787d896df567" class="bulleted-list"><li style="list-style-type:disc"><strong>수소충전소 압축기 현장 성능평가 가이드라인 개발</strong><br/><br/>산업부 국책 연구과제로, 기체 수소충전소의 핵심 설비인 압축설비의 상태진단과 성능평가를 통해 신뢰성을 확보하고자 기획된 과제입니다. 현재 국내 수소충전소의 압축기 타입은 피스톤, 다이아프램, 아이오닉 세가지 타입이 있으며, 각 타입별 압축기에 대한 고장분석을 수행하였습니다. <br/>수소충전소 압축기에서 가장 빈번하게 발생하는 고장은 수소누출이며, 수소누출이 발생 시 압축기 토출 압력, 토출 온도, 체적효율 이 세가지 변수에 주로 영향을 주기 때문에 이 변수들의 해석을 통해 수소누출을 감지할 수 있습니다. 감지방법으로 모델 기반 고장진단 기법인 관찰차 및 매개변수 잔차 비교법을 이용해 이상상태를 진단할 수 있습니다. 이상상태 지표로 다음 두 가지 잔차를 선정하였습니다. 첫번째는 센서로부터 측정한 값과 모델로부터 추정한 값의 잔차이며, 두번째는 모델로부터 추정한 매개변수와 공칭 매개변수의 잔차입니다. 우선 시뮬레이션 모델 구축을 위하여 Simulink 및 Simscape를 이용하여 수소충전소 전체 공정을 구축하였고, 모니터링시스템을 통해 수집한 제어로직 시퀀스를 입력신호로 설정하여 프로세스 값들을 추정하였습니다. 이후 압축기가 운전한 연속데이터에서 관찰자 기법으로 토출 압력 및 온도의 잔차를 구하고 매개변수 추정법으로 체적 효율의 잔차를 구할 수 있었습니다. 최종적으로 세가지 잔차에 대해 다변수 통계검정 기법인 Paired Hotelling T-squared 을 통해 잔차가 정상상태로부터 얼마나 벗어나 있는지 확인하여 수소누출을 감지하는 솔루션을 개발하였습니다.<br/></li></ul><div id="41a80007-a7f7-4c96-88a6-4996798ca89d" class="column-list"><div id="4c9c19d6-181c-43e8-b53a-88bffcab20f0" style="width:50%" class="column"><figure id="531c5d4c-0fd0-4d8d-8e39-d15fdf944d89" class="image"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%207.png"><img style="width:912px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%207.png"/></a><figcaption>Simscape-based hydrogen Refueling station Compression system model</figcaption></figure><p id="8f43c34f-4c9c-40d6-8f5d-219b44bdbc66" class="">
</p></div><div id="ae82dedd-3b65-4287-8abc-4c93173c38ad" style="width:50%" class="column"><figure id="19fd8b30-7480-4c8c-9110-4155a498c113" class="image"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%208.png"><img style="width:860px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%208.png"/></a><figcaption>Simscape based detailed model for parameter estimation</figcaption></figure></div></div><p id="465ce16d-0c69-4d52-8da3-83fd43a290c9" class="">
</p><div id="99249854-1d40-48ef-a3ea-71f4ac5fbb28" class="column-list"><div id="b1e633d0-ede0-45a3-a9d3-0b5ff05d3034" style="width:50%" class="column"><figure id="4715ec8f-6852-4758-9e03-1bd61913fe16" class="image"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%209.png"><img style="width:940px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%209.png"/></a><figcaption>Comparison of measured and simulated data of compressor pressure</figcaption></figure></div><div id="ded5bc69-4190-485e-8555-9b57839be687" style="width:50%" class="column"><figure id="6f55f85b-3747-4178-9657-c0ed872f32b8" class="image"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2010.png"><img style="width:866px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2010.png"/></a><figcaption>Graph of volumetric efficiency according to leakage in reciprocating compressor cylinder</figcaption></figure></div></div><figure id="d89c760c-dc76-403f-8d43-c24b9733e00d" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2011.png"><img style="width:864px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2011.png"/></a><figcaption>Comparison of measured and simulated data: (a) and (b) normal state and (c) and (d) Fault state</figcaption></figure><figure id="1b1ff9df-d85a-47e4-a8d0-c54a767e318a" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2012.png"><img style="width:1056px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2012.png"/></a><figcaption>Pair plot and 3D scatter plot of residuals by leak location</figcaption></figure><figure id="122af031-0efc-407d-9cbb-67f72e739b7c" class="image"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2013.png"><img style="width:480px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2013.png"/></a><figcaption>Confusion matrix results using neural network technique</figcaption></figure><p id="849b14ca-b033-420a-9dd5-94076faf9c4d" class="">
</p><p id="8913bc71-d264-40d9-81d1-69598f327494" class="">그리고 상태진단을 통해 즉각 알람을 발생시킬 수 있도록 시뮬레이션을 실시간으로 계산할 수 있는 아키텍처를 구축하였습니다. 시뮬레이션은 컴퓨터 리소스가 많이 필요한 모델이기 때문에 안정적으로 필요한 리소스를 할당받아 시스템이 가동될 수 있도록 클라우드 웹서비스인 AWS를 사용하였습니다. 설비의 상태정보를 IoT 통신기술을 이용해 실시간으로 수신할 수 있도록 AWS의 IoT Core을 사용하였으며, 수신한 신호를 곧바로 계산하여 시뮬레이션 추정값을 산출할 수 있도록 Lambda 모듈에 Simulink 모델을 입력하였고, 잔차 및 이상지표를 실시간으로 쿼리하여 대시보드에서 보여질 수 있도록 DynamoDB를 구축하였습니다.</p><figure id="bd1462d8-4a3f-486b-a381-38750b5226e3" class="image"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2014.png"><img style="width:720px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2014.png"/></a><figcaption>수소충전소 압축기 실시간 진단을 위한 Amazon Web Service 클라우드 시스템 아키텍처</figcaption></figure><p id="d5c27ccd-0b43-4e34-9b30-85d645698a64" class="">
</p><ul id="635783d6-e164-43b7-9d03-f439639d1656" class="bulleted-list"><li style="list-style-type:disc"><strong>수소충전소 설계 및 운전 안전성 검증 사전진단 프로그램 개발</strong><br/><br/>산업부 국책 연구과제로서, 정량적 위험성평가 및 공정해석 두 가지 기술을 활용해 수소충전소의 프로세스 설계 단계에서 안전성을 사전 검증하고자 기획된 과제입니다. 저는 주관기관의 실무 담당자로서 전체적인 프로젝트 목표 관리 및 기관들간의 협업 조율 등의 업무를 수행하였으며, 이와 함께 모델 기반 공정해석을 위해 시뮬레이션 모델 개발을 주도적으로 이끌었습니다. 액체 및 기체 수소충전소의 해석 모델을 구축하기 위한 프로그램으로는 Simulink 및 Simscape를 사용하였으며, 위험성 평가로부터 도출한 여러 테스트 케이스의 안전성 검증을 수행하였습니다..<br/><figure id="e738e965-9914-465c-a4e3-70cb03552ce2" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2015.png"><img style="width:912px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2015.png"/></a></figure><p id="f57315f2-3df8-427a-9f0f-7741d5398580" class="">
</p><p id="262dd4de-6d95-47c6-a87f-8d30aa31eec5" class="">그 중 수소충전 프로토콜을 개발한 경험이 있습니다. 수소 저장용기에 고압수소를 주입하면 온도 상승이 일어나 저장용기의 손상 및 폭발이 일어날 수 있는데, 이러한 위험을 차단하기 위해 차량 용기, 공급수소의 압력 및 온도 등 변수에 따른 APRR(평균 압력 상승 속도)을 조절하게 됩니다. 충전 속도가 느려 이용자의 불편을 유발하지 않으면서도 안전을 준수한 최적의 충전 프로세스를 수소충전 프로토콜에서 제시하기 때문에 수소충전 프로토콜은 프로세스 개발에 중요한 설계 요소 중 하나입니다. 현재 SAE J2601이 세계적으로 널리 적용되고 있으며, 충전온도 -40℃ 이상 85℃ 이하, 충전압력 0.5MPa 이상 87.5MPa 이하, 충전율 100% 이하, 충전속도 60g/s 이하라는 제한조건이 규정되어 있습니다. SAE J2601에는 저중량 용량의 모빌리티에 대해서만 APRR을 조절하는 제어로직이 포함되어 있어, 저희 연구에서는 대용량 모빌리티 등 국내 인프라 설비 현황을 고려하여 다양한 케이스에 대한 제어로직을 추가로 개발하였습니다. APRR 제어로직을 구현하기 위해 Simulink의 Stateflow를 이용하였으며, What-if Simulation으로 케이스 별 온도 상승을 추정하여 최적의 제어로직을 선정하였습니다. 또한 국부 고온부 발생 가능성을 확인하기위해 3D 시뮬레이션인 CFD를 이용하여 추가적인 안전성 검증을 수행하였습니다.</p><figure id="7d67520e-a5bb-4fa3-845a-87321010a7e9" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2016.png"><img style="width:864px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2016.png"/></a></figure><figure id="866994ba-f5dd-46fe-9c8b-70ca9b86ce36" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2017.png"><img style="width:816px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2017.png"/></a><figcaption>Simulink - Stateflow를 활용하여 수소 충전 프로토콜을 개발한 결과물입니다.</figcaption></figure><p id="45239c2a-3e9b-41da-bfb8-959906f55316" class="">
</p></li></ul><ul id="9a8a22a4-5cab-40e0-80c7-3ad5aae5456e" class="bulleted-list"><li style="list-style-type:disc"><strong>액화수소충전소 공정 최적화</strong><br/><br/>액화수소충전소에서 BOG 발생량 과다 및 냉매의 냉각불량 문제가 발생하여, 액화수소충전소 발주사에서 프로세스에 대해 문제해결과 최적화 용역 의뢰를 요청하여 수행하게된 프로젝트입니다. 저는 모델 기반 해석을 담당하여 Simulink 및 Simscape를 통해 액체수소충전소 전체 공정 모델을 구축하였습니다. 시운전 데이터의 제어로직 시퀀스를 입력신호로 설정하여 프로세스값을 추정하였고, 센서로부터 계측한 측정값과 모델로부터 추정한 값을 비교하며 어느 지점에서 에너지 손실이 발생했는지 파악하였습니다. 추정 결과, 에너지 손실 지점은 액체수소 펌프를 감싸는 캔에서 크게 발생하였으며, 이를 통해 캔과 주변 배관의 MLI를 보강하는 해결안을 제시할 수 있었습니다.<br/><br/>냉각불량 문제에 대해서는 기존 냉매의 어는점이 높아 과냉각시 유동성이 줄어드는 문제를 해결하기 위해 냉매를 교체해야하는 대체안이 제시되었으며, 대체된 냉매를 사용했을 시 성능을 검증하기 위해 열교환기 시스템을 모델링하였습니다. 열교환기 시스템을 모델링하기 위해 튜브 개수, 단면적, 길이와 같은 형상데이터가 필요한데, 이와 같은 엔지니어링 데이터가 주어지지 않아 파라미터를 입력할 수 없는 문제가 있었습니다. 대신 기존 냉매에 대한 성능 테스트 데이터가 있어, 입력 및 출력 신호를 Parameter Estimation 기법으로 열교환기 파라미터를 추정하여 모델링 할 수 있었습니다. 냉매는 액체수소의 냉열을 회수하여 수소를 기화시킨 후, 차량 충전 시 다시 수소의 온도를 낮추는 역할을 합니다. 이 때 가열된 냉매가 곧바로 냉매저장탱크로 회수되는 것보다는 중간 저장탱크를 두어 회수하면 열손실을 줄일 수 있을 것으로 판단하여, 중간 저장탱크를 추가한 모델을 구현하여 열손실 저감 효과를 검증하여 최적화 방안을 제시할 수 있었습니다.<br/><figure id="043c8912-9785-4d61-b46a-729d26fe2e8e" class="image"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2018.png"><img style="width:1080px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2018.png"/></a><figcaption>시뮬링크 모델로 구현한 액화수소충전소 냉각시스템입니다. 대체된 냉매를 사용했을 시 공정 시뮬레이션을 수행한 모습입니다.</figcaption></figure></li></ul><ul id="27128e11-6cb5-4987-9107-62fed99d429b" class="bulleted-list"><li style="list-style-type:disc"><strong>천연가스설비 신뢰성 향상을 위한 Big Data 시스템 개발</strong><ul id="d059e48a-3f69-4b7f-9947-806942a0b6f3" class="bulleted-list"><li style="list-style-type:circle">회전기기 잔류수명 평가 알고리즘 개발<br/><br/>천연가스설비 고압 원심펌프에 대해 진동데이터를 수집 및 분석하여 잔류수명평가를 수행하는 알고리즘 기법과 빅데이터 분석 시스템을 개발하였습니다. 진동데이터에서 17개의 특징변수를 추출하고 단조성과 같은 유사도 기반으로 열화 단계를 분류하였습니다. 또한 하둡 아키텍처를 활용하여 실시간 데이터를 수집하고(kafka) 배치단에서는 열화 단계를 계산하는 방법(Spark)으로 빅데이터 분석 시스템을 구현하였습니다.<br/></li></ul></li></ul><figure id="df6c17f0-667e-4d9c-9b7a-a4dab132749b" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2019.png"><img style="width:864px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2019.png"/></a></figure><figure id="d470c252-d8a9-4b19-b41f-92beb221a91f" class="image" style="text-align:center"><a href="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2020.png"><img style="width:528px" src="CV%20-%20Jinwoo%20Lee%2012269f3b13ea4c489998b5d534218645/Untitled%2020.png"/></a><figcaption>회전기기에서 진동데이터를 수집하여 데이터분석을 수행하는 프로세스 절차입니다.</figcaption></figure></div></article><span class="sans" style="font-size:14px;padding-top:2em"></span></body></html>
"""

# streamlit의 components.html을 사용하여 HTML 코드를 화면에 표시합니다.
st.components.v1.html(html_code)
