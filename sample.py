'''
Created on 
Course work: 
@author: Praabindh, Hari Prasad,Divya,Bairavi,Sharon
Source:
    
'''

# Import necessary modules

content = """WORD,DEFINITION,TV-SHOW-Line, TV-Show-Details
throw out, to get rid of as a useless, My wife threw me out, Two and Half Men Pilot
stay over, stay overnight, Is she staying over?, Two and Half Men Pilot
rigid, -, Rigid, 
musky, -, Your brother. He has a very musky scent,
suffocating, -, I'm not that suffocating guy you threw out of the house,
renaissance, -, A rebirth. A renaissance if you will,
bluffs, -, He always pulls his ear when he bluffs,
inherently, -, Is there something inherently wrong with,"""

def startpy():
    print('Hey there')

    # print(content)

    content_list = content.split('\n')

    # print(content_list)

    for cont in content_list:
        print(cont)


if __name__ == '__main__':
    startpy()