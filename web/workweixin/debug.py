from test_selenium.base import Base


class Testcookies(Base):
    def test_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        cookies = self.driver.get_cookies()
        print(cookies)
        return cookies
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1287582840365913'},
               {'domain': 'work.weixin.qq.com', 'expiry': 1603403500, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '21dkbv1'},
               {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1634907964, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'},
               {'domain': '.work.weixin.qq.com', 'expiry': 1605963966, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
