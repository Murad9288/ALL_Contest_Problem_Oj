# vaiyer problem...
# বর্ণনা: প্রথমে ২টি লিস্ট দেওয়া থাকবে। তারপর ২য়  লিস্টটি দিয়ে ১ম  লিস্টটিকে সার্চ করে বের করা লাগবে যে ,
# ২য় লিস্টটির উপাদান গুলো ১ম লিস্টটির কত নাম্বার পজিশনে -এ আছে। কিন্তু ২য়  লিস্টটির উপাদান গুলোর মধ্যে
# ১ম উপাদানটির পজিশন বের করার  পর ২য়  উপাদানটির পজিশন বের করার সময় ১ম উপাদানটিকে ১ম লিষ্টের
# মধ্যে ঐ উপাদানটিকে রিমুভ করে সামনে নিয়ে আসা লাগবে। আর এইভাবে ২য় লিস্টটির পরের উপাদান
# গুলোও বের করা লাগবে|
'''
li = [3,5,7,9,1,2,6]
n = [9,1,3,2]
for i in n:
     ind = li.index(i)
     print(ind + 1, end=" ")
     li.remove(i)
     li.insert(0, i)
 
'''
# input niyeo kora jay..

li = list(map(int,input().split()))
second_li = list(map(int,input().split()))
for i in second_li:
     index = li.index(i)
     print(index + 1, end=" ")
     li.remove(i)
     li.insert(0,i)


