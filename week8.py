import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data= pd.read_csv("GBvideos.csv")

##matplotlib plot
#x = data['channel_title'].head(5)
#y1 = data['views'].head(5)
#y2 = data['likes'].head(5)

#fig,ax = plt.subplots()

#ax.plot(x,y1, marker="v", linestyle="--", color="r")
#ax.plot(x,y2)


##seaborn plot
sns.lineplot(x=data['video_id'].head(25),
y=data['views'].head(25))


plt.show()




