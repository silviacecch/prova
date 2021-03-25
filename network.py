import pandas as pd
import json
import networkx as nx
import matplotlib.pyplot as plt 

def csv_to_json(csvFilePath, jsonFilePath):
        df = pd.read_csv("connessionidiprova.csv", sep=";")
        nodes=[]
        links=[]
        df1= df[df['likedBy_uniqueId']!= '-']
        print('nodes:')
        dictlist_nodes=list() 
        master_set = set()  
        for index, row in df1.iterrows():  
            newlist=list()              
            newlist.append(int(row['author_id'])) 
            newlist.append(row['author_uniqueId'])
            master_set.add(tuple(newlist))        
            newlist=list()
            newlist.append(int(row['likedBy_id']))  
            newlist.append(row['likedBy_uniqueId'])
            master_set.add(tuple(newlist))  
        master_list=list(master_set)  
        print(master_list)
        for i in master_list:
            dict_nodes = {   
                        "name":"",
                        "value":"",
                        "colour":""        
                }
            dict_nodes['value']=int(i[0])
            dict_nodes["name"] = i[1]
            dictlist_nodes.append(dict_nodes)
        nodes = dictlist_nodes
        print ((nodes))  
        print ('links:')
        dictlist_links=list()
        for index, row in df1.iterrows():
                dict_links = {
                        "target":"",
                        "source":"",
                        "value":1
                        }
                dict_links["target"] = int(row['author_id'])
                dict_links["source"] = int(row['likedBy_id'])
                dictlist_links.append(dict_links)
        links=dictlist_links 
        print (len(links))
        dictfinal={
            "nodes":dictlist_nodes,
            "links":dictlist_links
        }
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
                   #jsonString = json.dumps(jsonArray, indent=4)
                   #nodesString = json.dumps(nodes, indent=4)
                   dictString = json.dumps(dictfinal, indent=4)
                   jsonf.write(dictString)
          
csvFilePath = r'connessionidiprova.csv'
jsonFilePath = r'connessionidiprova.json'
csv_to_json(csvFilePath, jsonFilePath)
with open('connessionidiprova.json') as f:
    data = json.load(f)
    n_nodes=len(data['nodes']) #numero di nodi del grafo
    n_edges=len(data['links']) #numero di archi del grafo
    nodes_names=[] #qui ci andranno i nomi dei personaggi
    nodes=[] #qui ci andranno i codici dei personaggi nello stesso ordine dei nomi
    edges=[] #qui ci andrà la lista di liste (con ogni lista arco composto da nodo 1 nodo 2 e peso)
    for i in range(n_nodes):
        nodes.append(i)
        nodes_names.append(data['nodes'][i]['name'])
    for i in range(n_edges):
        list_to_append=[]
        source=data['links'][i]['source']
        target=data['links'][i]['target']
        value = data['links'][i]['value']
        list_to_append.append(source)
        list_to_append.append(target)
        list_to_append.append(value)
        edges.append(list_to_append)
      
plt.figure(figsize=(35,45))
graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)
pos = nx.spring_layout(graph)
nx.draw_networkx_nodes(graph,pos,node_color='limegreen',node_size=10)
nx.draw_networkx_edges(graph,pos)#edge_color='lightgrey'
labels={} 
for i in range(len(nodes_names)):
    labels[i] = nodes_names[i]
#nx.draw_networkx_labels(graph,pos,labels,font_size=12)
#edge_labels = nx.get_edge_attributes(graph, "weight")
#nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
plt.show()
