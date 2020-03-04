# 计算给定经纬度的两点之间的方位角与大圆距离

from geographiclib.geodesic import Geodesic

lat1=float(input("请输入当前位置纬度："))
lon1=float(input("请输入当前位置经度："))
lat2=float(input("请输入目标地点纬度："))
lon2=float(input("请输入目标地点经度："))

data=Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)

print("您与目标地的方位角为%f°"%data['azi1'])
print("您与目标地的大圆距离为%f米"%data['s12'])

# print("您距目标地的距离为%f米"%data['s12'])
# print("您距目标地的距离为%f米"%data['s12'])
# print("您距目标地的距离为%f米"%data['s12'])
