startTime=0
endTime=0
length=3697
i=0
while [ $endTime -le $length ]; do
  #statements
  i=$[$i+1]
  endTime=$[$startTime+10]
  ffmpeg -i p2.mp4  -ss $startTime -to $endTime -acodec copy -vcodec libx264 -preset fast -b 10000k $i.mp4
  startTime=$[endTime]
done