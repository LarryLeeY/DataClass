#coding = utf-8
'''
lbllist: the list object of lalbel trian labels
'''
def cnt_train_sample_size(lbl_list):
	lbl_set = set(lbl_list)
	lbl_cnt = []
	
	for lbl in lbl_set:
		lbl_num = lbl_list.count(lbl)
		lbl_cnt.append({
			'value' : lbl_num,
			'name'  : lbl
			})

	piedata = {
		"legend": list(lbl_set),
		"data": lbl_cnt
	}
	return piedata

'''
data : test data
lbls : predicted labels 
'''
def format_test_series(data, lbls):
	cls_result = {}
	for point, lbl in zip(data, lbls):
		if lbl not in cls_result.keys():
			cls_result[lbl] = []
			cls_result[lbl].append(point)
		else:
			cls_result[lbl].append(point)

 	series = []
 	
 	for name in cls_result.keys():
 		series.append({
 			'name' : name,
 			'data' : cls_result[name],
 			'type' : 'scatter'
 			})
	
	return series
'''
input : str  To check the datasets is valid.
return : bool 
'''
def is_vaild(input_value):
	input_to_list = input_value.split(',')
	input_to_set  = set(input_to_list)

	for item in input_to_set:
		if not item.isdigit():
			return False

	return True

import numpy as np

def str2matrix(data, dim):
	data_list = data.split(',')
	data_num = [int(elm) for elm in data_list]
	row_num = len(data_num) / dim
	matrix =  np.array(data_num).reshape(row_num, dim)
	return matrix

def str2list(data):
	return str2matrix(data, 1)
