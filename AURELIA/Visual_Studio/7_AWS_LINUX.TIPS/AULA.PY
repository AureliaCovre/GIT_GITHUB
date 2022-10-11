""" 
CHARACTERISTICS AND ADVANTAGES  
- Agility
- Maintenance
- Reliability
- Security
- Performance
- Scalability
- Cost and Elasticity
"""

""" SERVICE MODELS 
- Iaas: Infraestruturas como serviços (não tinha a estrutura instalada, usava a de alguem)
- Paas: Plataforma como serviço ()
- Faas: Função como serviço
"""

""" DEPLOYMENT MODELS
- Private Cloud: Um Cloud que é seu 
- Public Cloud: Qqer um pode usar. (A plataforma que  está provendo, ex.: aws, google cloud)
- Hybrid Cloud:  Quer dizer que tem 2 empresas cloud rodando meu serviço
- *Multicloud: Você roda todos os seus serviços em todos os clouds. 
- Community: Empresas se reunem e constroem um cloud para q mais de uma empresa use. 
"""



segundos = int(input("segundos: "))

horas = int(segundos / 3600)
print("horas: ",horas)
resto_h = int(horas - segundos)
segundos = resto_h

minutos = int(segundos / 60)
print("minutos", minutos)