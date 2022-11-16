import re

c = 'rgba(0, 0, 0, 0) url("http://test.exlab.team/images/logo/logo_black.png") repeat scroll 0% 0% / auto padding-box border-box'

pattern = r"\s+"
#re_c = re.split('[()]', c)[3].replace('"','')
#
#print(re_c)

back_dark = 'rgb(17, 17, 17) none repeat scroll 0% 0% / auto padding-box border-box'

re_b = re.split('[()]', back_dark)

print(re_b[1])#

