#coding = utf-8
import random
def gendata(xmin, xmax, ymin, ymax):
	x_axis = random.randint(xmin, xmax)
	y_axis = random.randint(ymin, ymax)
	return [x_axis, y_axis]

if __name__ == "__main__":
	data = open('test.csv', 'w')
	label = open('tlabel.csv', 'w')

	for i in range(0, 5):
		cls_one =  gendata(0, 50, 0, 50)
		data.write(str(cls_one[0]) + ',' + str(cls_one[1]) + '\n')
		label.write('1\n')
		cls_two =  gendata(50, 100, 0, 50)
		label.write('2\n')
		data.write(str(cls_two[0]) + ',' + str(cls_two[1]) + '\n')
		cls_three = gendata(0, 50, 50, 100)
		label.write('3\n')
		data.write(str(cls_three[0]) + ',' + str(cls_three[1]) + '\n')
		cls_four =  gendata(50, 100, 50, 100)
		data.write(str(cls_four[0]) + ',' + str(cls_four[1]) + '\n')
		label.write('4\n')

	data.close()
	label.close()