# This script was not written by MicroPasts but rather is porvided
# courtesy of Agisoft and Lee Perry-Smith

# Compatibility from PhotoScan Pro 0.9.1 (starting from build 1703)

# If this script is put in the following folder (on Windows):
# C:/users/<user name>/AppData/Local/AgiSoft/PhotoScan Pro/scripts
# it will create a custom menu item.

import PhotoScan 
import math

def main():



	doc = PhotoScan.app.document

	for i in range(len(doc.chunks)):
		chunk = doc.chunks[i]

		R = chunk.region.rot
		C = chunk.region.center

		if chunk.transform:
			T = chunk.transform
			s = math.sqrt(T[0,0]*T[0,0] + T[0,1]*T[0,1] + T[0,2]*T[0,2])
			S = PhotoScan.Matrix( [[s, 0, 0, 0], [0, s, 0, 0], [0, 0, s, 0], [0, 0, 0, 1]] )
		else:
			S = PhotoScan.Matrix( [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]] )

		T = PhotoScan.Matrix( [[R[0,0],R[0,1],R[0,2], C[0]], [R[1,0],R[1,1],R[1,2],C[1]], [R[2,0],R[2,1],R[2,2],C[2]], [0,0,0,1]])

		xm = PhotoScan.Matrix( [[1,0,0,0],[0,0,-1,0],[0,1,0,0],[0,0,0,1]] )
		ym = PhotoScan.Matrix( [[0,0,-1,0],[0,1,0,0],[1,0,0,0],[0,0,0,1]] )
		zm = PhotoScan.Matrix( [[0,-1,0,0],[1,0,0,0],[0,0,1,0],[0,0,0,1]] )


		chunk.transform = ym * xm * S * T.inv()
		
		#Rotation matrices (by 90 degrees):
		# the use chunk.transform = zm * S * T.inv()
	print("Script finished. Coordinate system is now parallel to Bounding Box\n")
	
PhotoScan.app.addMenuItem("Custom menu/Coordinates to bounding box + rotate", main)	
