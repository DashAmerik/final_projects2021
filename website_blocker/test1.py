
def BlockedWebsiteRead():
    f = open('c:\windows\system32\drivers\etc\hosts','r')
    file = f.readlines()
    f.close()
    website = []
    for i in range(len(file)):
        if '#' not in file[i] and 'www' in file[i]:
            element = file[i]
            element = element.split()
            website.append(element[1])
    return website, file

def BlockNewWebsite():
    user_input = input("what website do you want to block: ")

    f = open('c:\windows\system32\drivers\etc\hosts','a')
    f.write('\n'+'127.0.0.1'+' '+user_input)
    f.close()

def UnblockWebsite(website, file):
    user_input = input("what website do you want to unblock: ")
    if user_input in website:
        website.remove(user_input)
    f = open('c:\windows\system32\drivers\etc\hosts','a')
    print(file)
    if user_input in file:
        file.remove(user_input)
    file = "".join(file)
    f.write(file)
    f.close()
    return website




website,file = BlockedWebsiteRead()
print("the websites that are currently blocked are:")
for i in range(len(website)):
    print(website[i])

action = input("What would you like to do? [b/u]: ")
if action == 'b':
    BlockNewWebsite()
    website2 = BlockedWebsiteRead()
if action == 'u':
    website2 = UnblockWebsite(website,file)
print("the websites that are currently blocked are:")
for i in range(len(website2)):
    print(website2[i])
