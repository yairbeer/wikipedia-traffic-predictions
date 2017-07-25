import pandas as pd


class TrainHandler:
    def __init__(self, train_filename):
        self.train = pd.DataFrame.from_csv(train_filename)

# "Page","2015-07-01","2015-07-02","2015-07-03","2015-07-04","2015-07-05","2015-07-06","2015-07-07","2015-07-08","2015-07-09","2015-07-10","2015-07-11","2015-07-12","2015-07-13","2015-07-14","2015-07-15","2015-07-16","2015-07-17","2015-07-18","2015-07-19","2015-07-20","2015-07-21","2015-07-22","2015-07-23","2015-07-24","2015-07-25","2015-07-26","2015-07-27","2015-07-28","2015-07-29","2015-07-30","2015-07-31","2015-08-01","2015-08-02","2015-08-03","2015-08-04","2015-08-05","2015-08-06","2015-08-07","2015-08-08","2015-08-09","2015-08-10","2015-08-11","2015-08-12","2015-08-13","2015-08-14","2015-08-15","2015-08-16","2015-08-17","2015-08-18","2015-08-19","2015-08-20","2015-08-21","2015-08-22","2015-08-23","2015-08-24","2015-08-25","2015-08-26","2015-08-27","2015-08-28","2015-08-29","2015-08-30","2015-08-31","2015-09-01","2015-09-02","2015-09-03","2015-09-04","2015-09-05","2015-09-06","2015-09-07","2015-09-08","2015-09-09","2015-09-10","2015-09-11","2015-09-12","2015-09-13","2015-09-14","2015-09-15","2015-09-16","2015-09-17","2015-09-18","2015-09-19","2015-09-20","2015-09-21","2015-09-22","2015-09-23","2015-09-24","2015-09-25","2015-09-26","2015-09-27","2015-09-28","2015-09-29","2015-09-30","2015-10-01","2015-10-02","2015-10-03","2015-10-04","2015-10-05","2015-10-06","2015-10-07","2015-10-08","2015-10-09","2015-10-10","2015-10-11","2015-10-12","2015-10-13","2015-10-14","2015-10-15","2015-10-16","2015-10-17","2015-10-18","2015-10-19","2015-10-20","2015-10-21","2015-10-22","2015-10-23","2015-10-24","2015-10-25","2015-10-26","2015-10-27","2015-10-28","2015-10-29","2015-10-30","2015-10-31","2015-11-01","2015-11-02","2015-11-03","2015-11-04","2015-11-05","2015-11-06","2015-11-07","2015-11-08","2015-11-09","2015-11-10","2015-11-11","2015-11-12","2015-11-13","2015-11-14","2015-11-15","2015-11-16","2015-11-17","2015-11-18","2015-11-19","2015-11-20","2015-11-21","2015-11-22","2015-11-23","2015-11-24","2015-11-25","2015-11-26","2015-11-27","2015-11-28","2015-11-29","2015-11-30","2015-12-01","2015-12-02","2015-12-03","2015-12-04","2015-12-05","2015-12-06","2015-12-07","2015-12-08","2015-12-09","2015-12-10","2015-12-11","2015-12-12","2015-12-13","2015-12-14","2015-12-15","2015-12-16","2015-12-17","2015-12-18","2015-12-19","2015-12-20","2015-12-21","2015-12-22","2015-12-23","2015-12-24","2015-12-25","2015-12-26","2015-12-27","2015-12-28","2015-12-29","2015-12-30","2015-12-31","2016-01-01","2016-01-02","2016-01-03","2016-01-04","2016-01-05","2016-01-06","2016-01-07","2016-01-08","2016-01-09","2016-01-10","2016-01-11","2016-01-12","2016-01-13","2016-01-14","2016-01-15","2016-01-16","2016-01-17","2016-01-18","2016-01-19","2016-01-20","2016-01-21","2016-01-22","2016-01-23","2016-01-24","2016-01-25","2016-01-26","2016-01-27","2016-01-28","2016-01-29","2016-01-30","2016-01-31","2016-02-01","2016-02-02","2016-02-03","2016-02-04","2016-02-05","2016-02-06","2016-02-07","2016-02-08","2016-02-09","2016-02-10","2016-02-11","2016-02-12","2016-02-13","2016-02-14","2016-02-15","2016-02-16","2016-02-17","2016-02-18","2016-02-19","2016-02-20","2016-02-21","2016-02-22","2016-02-23","2016-02-24","2016-02-25","2016-02-26","2016-02-27","2016-02-28","2016-02-29","2016-03-01","2016-03-02","2016-03-03","2016-03-04","2016-03-05","2016-03-06","2016-03-07","2016-03-08","2016-03-09","2016-03-10","2016-03-11","2016-03-12","2016-03-13","2016-03-14","2016-03-15","2016-03-16","2016-03-17","2016-03-18","2016-03-19","2016-03-20","2016-03-21","2016-03-22","2016-03-23","2016-03-24","2016-03-25","2016-03-26","2016-03-27","2016-03-28","2016-03-29","2016-03-30","2016-03-31","2016-04-01","2016-04-02","2016-04-03","2016-04-04","2016-04-05","2016-04-06","2016-04-07","2016-04-08","2016-04-09","2016-04-10","2016-04-11","2016-04-12","2016-04-13","2016-04-14","2016-04-15","2016-04-16","2016-04-17","2016-04-18","2016-04-19","2016-04-20","2016-04-21","2016-04-22","2016-04-23","2016-04-24","2016-04-25","2016-04-26","2016-04-27","2016-04-28","2016-04-29","2016-04-30","2016-05-01","2016-05-02","2016-05-03","2016-05-04","2016-05-05","2016-05-06","2016-05-07","2016-05-08","2016-05-09","2016-05-10","2016-05-11","2016-05-12","2016-05-13","2016-05-14","2016-05-15","2016-05-16","2016-05-17","2016-05-18","2016-05-19","2016-05-20","2016-05-21","2016-05-22","2016-05-23","2016-05-24","2016-05-25","2016-05-26","2016-05-27","2016-05-28","2016-05-29","2016-05-30","2016-05-31","2016-06-01","2016-06-02","2016-06-03","2016-06-04","2016-06-05","2016-06-06","2016-06-07","2016-06-08","2016-06-09","2016-06-10","2016-06-11","2016-06-12","2016-06-13","2016-06-14","2016-06-15","2016-06-16","2016-06-17","2016-06-18","2016-06-19","2016-06-20","2016-06-21","2016-06-22","2016-06-23","2016-06-24","2016-06-25","2016-06-26","2016-06-27","2016-06-28","2016-06-29","2016-06-30","2016-07-01","2016-07-02","2016-07-03","2016-07-04","2016-07-05","2016-07-06","2016-07-07","2016-07-08","2016-07-09","2016-07-10","2016-07-11","2016-07-12","2016-07-13","2016-07-14","2016-07-15","2016-07-16","2016-07-17","2016-07-18","2016-07-19","2016-07-20","2016-07-21","2016-07-22","2016-07-23","2016-07-24","2016-07-25","2016-07-26","2016-07-27","2016-07-28","2016-07-29","2016-07-30","2016-07-31","2016-08-01","2016-08-02","2016-08-03","2016-08-04","2016-08-05","2016-08-06","2016-08-07","2016-08-08","2016-08-09","2016-08-10","2016-08-11","2016-08-12","2016-08-13","2016-08-14","2016-08-15","2016-08-16","2016-08-17","2016-08-18","2016-08-19","2016-08-20","2016-08-21","2016-08-22","2016-08-23","2016-08-24","2016-08-25","2016-08-26","2016-08-27","2016-08-28","2016-08-29","2016-08-30","2016-08-31","2016-09-01","2016-09-02","2016-09-03","2016-09-04","2016-09-05","2016-09-06","2016-09-07","2016-09-08","2016-09-09","2016-09-10","2016-09-11","2016-09-12","2016-09-13","2016-09-14","2016-09-15","2016-09-16","2016-09-17","2016-09-18","2016-09-19","2016-09-20","2016-09-21","2016-09-22","2016-09-23","2016-09-24","2016-09-25","2016-09-26","2016-09-27","2016-09-28","2016-09-29","2016-09-30","2016-10-01","2016-10-02","2016-10-03","2016-10-04","2016-10-05","2016-10-06","2016-10-07","2016-10-08","2016-10-09","2016-10-10","2016-10-11","2016-10-12","2016-10-13","2016-10-14","2016-10-15","2016-10-16","2016-10-17","2016-10-18","2016-10-19","2016-10-20","2016-10-21","2016-10-22","2016-10-23","2016-10-24","2016-10-25","2016-10-26","2016-10-27","2016-10-28","2016-10-29","2016-10-30","2016-10-31","2016-11-01","2016-11-02","2016-11-03","2016-11-04","2016-11-05","2016-11-06","2016-11-07","2016-11-08","2016-11-09","2016-11-10","2016-11-11","2016-11-12","2016-11-13","2016-11-14","2016-11-15","2016-11-16","2016-11-17","2016-11-18","2016-11-19","2016-11-20","2016-11-21","2016-11-22","2016-11-23","2016-11-24","2016-11-25","2016-11-26","2016-11-27","2016-11-28","2016-11-29","2016-11-30","2016-12-01","2016-12-02","2016-12-03","2016-12-04","2016-12-05","2016-12-06","2016-12-07","2016-12-08","2016-12-09","2016-12-10","2016-12-11","2016-12-12","2016-12-13","2016-12-14","2016-12-15","2016-12-16","2016-12-17","2016-12-18","2016-12-19","2016-12-20","2016-12-21","2016-12-22","2016-12-23","2016-12-24","2016-12-25","2016-12-26","2016-12-27","2016-12-28","2016-12-29","2016-12-30","2016-12-31"
# "2NE1_zh.wikipedia.org_all-access_spider",18,11,5,13,14,9,9,22,26,24,19,10,14,15,8,16,8,8,16,7,11,10,20,18,15,14,49,10,16,18,8,5,9,7,13,9,7,4,11,10,5,9,9,9,9,13,4,15,25,9,5,6,20,3,14,46,5,5,13,4,9,10,9,11,11,11,9,15,5,10,7,4,8,9,10,6,13,16,6,24,9,11,12,8,14,6,6,11,14,6,10,20,7,15,8,15,5,8,8,5,11,165,34,6,13,8,9,11,26,18,3,5,12,6,16,19,9,10,11,11,7,9,10,24,6,6,8,16,13,10,10,6,5,20,6,47,9,9,12,11,17,15,14,11,97,11,12,11,14,15,12,104,5,22,45,75,29,34,20,12,25,9,62,20,19,8,23,13,16,34,36,11,18,12,24,30,27,44,35,53,11,26,13,18,9,16,6,19,20,19,22,30,14,16,22,15,15,26,16,13,27,18,13,32,31,16,38,18,9,14,10,24,8,15,18,10,23,17,11,26,14,8,12,9,11,34,17,29,11,9,14,21,12,11,13,11,13,16,13,19,21,14,11,35,18,42,15,5,21,56,9,20,17,18,8,9,17,9,10,14,17,6,18,13,11,12,11,8,15,11,20,59,11,18,17,12,14,13,9,490,189,102,38,126,71,21,57,79,17,17,23,16,23,18,22,44,6,31,17,25,40,19,15,15,29,18,16,13,20,22,19,11,50,22,39,23,21,23,22,16,19,35,16,12,15,13,14,10,21,20,19,14,12,15,17,16,21,27,13,11,15,14,18,18,10,11,14,18,14,13,17,15,14,234,8,62,26,22,8,22,15,69,11,18,23,12,20,17,15,16,18,21,15,30,115,56,45,17,18,15,18,14,15,15,24,22,18,30,12,13,18,17,31,26,29,12,19,19,57,17,20,49,10,19,26,41,23,30,55,17,24,14,12,49,42,37,13,30,20,33,20,14,40,15,18,26,8,25,21,20,25,19,23,18,19,18,55,16,65,11,11,13,20,21,13,24,20,13,32,16,10,13,44,17,13,72,40,19,14,13,12,14,10,26,13,22,14,23,12,8,50,13,10,16,14,10,24,10,20,10,26,25,16,19,20,12,19,50,16,30,18,25,14,20,8,67,13,41,10,21,13,8,15,14,12,6,11,10,42,21,24,14,11,204,14,45,33,28,18,14,47,15,14,18,20,14,16,14,20,60,22,15,17,19,18,21,21,47,65,17,32,63,15,26,14,20,22,19,18,20
# "2PM_zh.wikipedia.org_all-access_spider",11,14,15,18,11,13,22,11,10,4,41,65,57,38,20,62,44,15,10,47,24,17,22,9,39,13,11,12,21,19,9,15,33,8,8,7,13,2,23,12,27,27,36,23,58,80,60,69,42,161,94,77,78,20,24,13,14,26,8,82,22,11,81,37,9,40,47,18,23,6,2,7,16,10,34,14,31,20,23,14,16,34,15,30,13,30,15,25,17,8,12,17,10,21,18,30,13,7,15,23,20,15,9,47,14,11,16,12,7,15,14,12,18,29,39,11,14,28,17,20,17,36,13,11,14,14,14,33,14,13,18,13,11,8,10,11,81,14,20,6,16,18,9,12,10,8,11,14,47,13,13,6,10,8,8,8,18,31,16,15,10,13,9,32,161,6,20,8,11,13,8,19,7,9,16,11,6,38,11,17,13,12,12,9,7,15,14,14,11,13,12,12,24,15,38,18,26,15,12,14,40,19,13,39,19,16,19,11,76,14,19,26,19,17,30,17,17,17,19,11,175,10,5,12,7,12,14,19,11,19,17,15,19,15,9,20,6,11,6,15,20,35,34,21,17,22,26,16,16,28,19,17,15,11,7,15,11,36,16,22,18,46,17,15,17,12,17,14,15,14,15,28,36,23,12,25,18,18,16,20,17,16,13,15,19,14,20,37,16,15,11,42,10,14,61,39,17,17,41,35,16,9,64,22,22,66,33,30,16,18,45,17,88,23,18,12,12,13,13,5,11,13,11,22,10,13,17,10,14,18,9,16,17,6,15,18,10,11,16,10,12,12,13,9,16,19,19,11,15,10,20,25,9,14,10,14,18,25,13,24,14,13,14,24,16,15,13,11,12,28,28,17,27,48,184,64,24,92,31,34,49,21,36,32,16,16,19,22,22,19,18,18,17,35,49,19,25,24,39,19,29,30,16,54,15,39,19,17,60,12,77,63,12,9,34,30,13,20,29,10,14,23,15,12,25,22,144,31,31,17,66,78,19,44,43,35,13,13,25,15,37,38,22,28,19,46,24,22,43,58,26,20,27,35,20,31,24,24,94,18,20,18,16,38,54,29,49,25,72,144,36,97,179,29,12,21,42,53,41,19,25,19,15,21,21,27,33,15,24,13,11,14,26,11,21,14,14,54,5,10,12,11,14,28,23,20,9,12,11,14,14,15,15,11,20,13,19,621,57,17,23,19,21,47,28,22,22,65,27,17,17,13,9,18,22,17,15,22,23,19,17,42,28,15,9,30,52,45,26,20
# "3C_zh.wikipedia.org_all-access_spider",1,0,1,1,0,4,0,3,4,4,1,1,1,6,8,6,4,5,1,2,3,8,8,6,6,2,2,3,2,4,3,3,5,3,5,4,2,5,1,4,5,0,0,7,3,5,1,6,2,5,0,3,1,0,1,1,2,4,2,1,1,3,4,3,6,6,4,3,3,2,9,7,2,3,1,3,1,6,7,1,2,5,2,3,8,5,0,4,1,5,3,0,1,8,2,1,3,0,0,5,3,3,0,2,5,2,5,10,5,6,1,4,4,1,3,13,2,1,3,2,1,10,5,6,2,5,2,2,3,2,6,3,2,1,2,3,1,1,2,2,3,2,2,5,7,2,3,4,6,1,3,6,3,3,4,2,2,4,3,1,5,5,4,2,4,5,4,2,1,6,1,1,3,1,3,5,3,3,0,5,3,2,2,2,2,0,3,3,3,4,4,8,3,5,8,1,4,0,3,6,3,1,3,3,3,1,3,8,4,3,2,5,6,3,6,5,6,7,3,1,5,1,2,0,1,4,3,3,9,4,7,5,10,2,3,3,4,2,3,5,3,6,4,5,5,2,1,4,7,2,2,5,1,0,3,3,1,2,4,2,2,3,4,7,1,1,10,9,5,1,6,7,4,6,2,4,155,155,83,48,31,16,6,13,8,8,5,7,3,4,6,7,10,9,7,8,4,6,5,2,7,3,7,6,3,1,6,2,1,3,8,3,5,4,7,5,2,5,0,3,12,4,2,4,6,4,5,9,4,5,7,1,5,1,5,4,5,7,7,5,3,4,1,9,3,4,6,2,2,1,16,6,3,3,6,1,6,1,4,3,5,1,6,5,1,4,5,4,2,4,3,4,2,0,1,3,12,4,7,5,6,6,6,3,3,3,5,5,2,11,6,2,2,3,7,5,4,5,3,3,9,7,2,1,5,6,7,13,3,5,6,2,4,1,2,7,2,2,4,4,2,5,3,2,3,5,4,2,5,7,5,2,7,6,11,10,5,19,7,11,4,10,3,4,6,3,4,8,10,3,3,1,10,5,4,4,3,4,1,3,6,6,6,3,5,11,6,3,7,6,0,2,4,4,3,6,4,3,4,1,6,5,5,2,3,3,2,2,6,1,3,3,3,2,10,2,2,2,7,3,6,4,2,4,6,5,4,4,3,3,9,3,5,4,0,1,4,5,8,8,1,1,2,5,3,3,3,7,3,9,8,3,210,5,4,6,2,2,4,3,3,1,1,7,4,4,6,3,4,17
# "4minute_zh.wikipedia.org_all-access_spider",35,13,10,94,4,26,14,9,11,16,16,11,23,145,14,17,85,4,30,22,9,10,11,7,7,11,9,11,44,8,14,19,10,17,17,10,7,10,1,8,27,19,16,2,84,22,14,47,25,14,11,12,27,8,17,43,3,19,14,20,43,4,5,37,23,14,12,13,22,12,12,6,27,5,7,24,8,9,10,12,19,7,7,18,15,7,9,10,9,14,8,17,6,8,7,5,3,9,5,6,8,8,11,6,7,28,15,8,7,7,12,5,11,3,7,23,6,3,8,8,39,4,10,6,8,9,16,9,8,8,7,5,5,12,8,15,9,12,5,7,6,12,7,6,33,5,11,6,4,32,9,17,2,10,10,5,7,11,8,10,6,17,11,20,11,15,18,10,15,12,12,12,8,13,9,11,4,12,9,6,12,9,9,6,7,7,11,7,14,9,21,9,10,13,10,13,16,8,10,7,13,18,8,50,8,33,6,22,9,84,28,11,7,14,16,49,71,29,22,6,34,16,14,9,12,24,18,8,26,8,8,13,21,9,10,14,12,9,10,20,15,26,24,19,10,12,8,16,13,8,17,12,34,10,9,9,15,10,12,8,11,9,28,17,11,13,10,10,10,16,12,12,13,25,25,18,18,23,27,39,11,16,9,26,14,15,10,23,17,74,114,8,15,15,15,12,14,14,23,21,11,19,9,10,11,14,9,5,10,20,22,16,9,10,42,22,7,7,54,7,9,13,5,10,12,18,23,23,17,6,14,13,13,9,11,35,8,12,15,10,25,9,8,8,10,14,9,11,303,29,121,69,39,25,27,54,39,24,22,20,14,12,8,17,11,15,19,20,11,36,19,35,22,14,17,15,12,34,20,25,15,18,19,13,17,16,11,22,43,8,13,16,8,19,14,9,13,13,16,10,10,11,17,32,21,16,23,15,55,17,17,15,7,13,11,11,8,22,5,7,18,9,13,27,15,19,7,9,14,14,9,16,11,7,14,13,11,9,9,9,11,15,28,10,24,8,20,19,12,31,14,9,40,15,83,60,19,15,15,12,23,17,20,26,11,13,9,44,7,18,4,36,34,10,8,21,7,6,12,15,9,13,21,13,10,21,15,103,22,15,12,11,15,7,12,13,9,8,21,16,38,13,14,17,26,14,10,9,23,15,7,10,7,10,14,17,11,9,11,5,10,8,17,13,23,40,16,17,41,17,8,9,18,12,12,18,13,18,23,10,32,10,26,27,16,11,17,19,10,11
# "52_Hz_I_Love_You_zh.wikipedia.org_all-access_spider",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,38,159,9,4,1,10,9,2,0,5,0,3,55,234,57,5,4,4,0,9,9,6,6,6,10,7,5,4,6,4,2,6,5,3,3,2,5,5,8,8,6,3,7,7,6,6,2,8,3,7,8,3,4,5,2,1,1,1,2,8,6,1,0,4,2,6,2,2,2,1,5,2,2,2,3,10,1,3,4,2,3,4,1,1,9,0,1,6,2,5,2,2,3,2,11,1,4,4,2,10,5,3,10,2,5,7,2,5,8,2,5,1,1,2,6,6,2,1,3,2,3,4,3,2,0,13,4,2,4,3,3,1,3,5,2,3,2,4,3,39,4,3,1,5,5,5,5,8,15,13,63,2,2,3,6,10,2,8,4,3,3,6,4,1,5,9,1,6,4,0,4,9,6,8,13,4,7,6,9,3,21,6,13,10,2,3,6,7,10,6,6,4,173,5,10,10,18,20,11,5,6,33,13,10,22,11,8,4,10,13,11,8,6,10,14,6,9,6,16,14,13,15,14,16,9,178,64,12,10,11,6,8,7,9,8,5,11,8,4,15,5,8,8,6,7,15,4,11,7,48,9,25,13,3,11,27,13,36,10