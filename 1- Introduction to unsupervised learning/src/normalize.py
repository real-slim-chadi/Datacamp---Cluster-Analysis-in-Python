from scipy.cluster.vq import whiten

goals_for = [4,3,2,3,1,1,2,0,1,4]

#scaling
sacled_data=whiten(goals_for)


print(sacled_data)

# IT WORKED :)