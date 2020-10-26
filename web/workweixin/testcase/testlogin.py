#!/usr/bin/env python
# -*- coding: utf-8 -*-
from web.workweixin.public.base_page import BasePage
from web.workweixin.page.login_index import IndexPage

class TestWX:
    def setup(self):
        self.index = IndexPage()
    def test_register(self):
        # assert self.index.goto_login().goto_register().register()
        assert self.index.goto_login().goto_register().register_success()