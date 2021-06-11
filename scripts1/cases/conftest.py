# -*- encoding: utf-8 -*-
'''
@File    :   conftest.py
@Time    :   2020/10/26 09:31:04
@Author  :   Jadenyu 
@Version :   Python 3.7.6
@State   :   None 
'''

# here put the import lib

import pytest
from py._xmlgen import html
from datetime import datetime


def pytest_addoption(parser):
    parser.addoption("--test_host", action="store", default="deeptables",
                     help="one of: deeptables, gbm")


@pytest.fixture
def test_host(request):
    return request.config.getoption("--test_host")


@pytest.mark.optionalhook
def pytest_html_results_summary(prefix):
    prefix.extend([html.p("所属部门: 开发管理中心")])
    prefix.extend([html.p("测试人员: 测试组")])


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(3, html.th('Time', class_='sortable time', col='time'))
    #cells.insert(1,html.th("Test_nodeid"))
    cells.pop()

@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    #cells.insert(2, html.td(report.description))
    cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
    #cells.insert(1,html.td(report.nodeid))
    cells.pop()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
    report.nodeid = report.nodeid #.encode("utf-8").decode("unicode_escape")   #设置编码显示中文
