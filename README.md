# BACKUP HUAWEI (ROUTER / SWITCH)

## Backup Routers e Switchs Huawei

#### Arquivo: backup-huawei-ne.py
Script em python3, metodo de uso:
```
# backup-huawei.py {IP} {USUARIO_SSH} {SENHA} {PORTA} {IDENTIFICACAO} {TIPO router/switch}
```
##### Os comandos executados são:
Para routers:
```
display current-configuration | no-more
```
Para Switchs:
```
screen-length 0 temporary
display current-configuration
```
#### Arquivo: DISPOSITIVOS
Com base nisso crie um arquivo com a lista de todos seus routes e switchs qual devem gerar backups:
```
IP,USUARIO,SENHA,PORTA,IDENTIFICACAO,TIPO
172.19.1.1,root,123456,22,NE_8K_VS_BORDA,router
172.19.1.2,root,123456,22,SWT_CORE_S6730,switch
```

### Arquivo gerabackup.sh
Iremos gerar um <b>for</b> executando o backup-fkw.py em toda nossa lista.
Ajuste o mesmo informado em <b>DIR</b> ex /root/scripts/BackupHuawei o local onde fica seu script.
Ajuste a váriavel <b>DIRSAVE</b> para o caminho qual deseja salvar seus backups. 
Será salvo um arquivo para cada equipamento no formato  aaaa-mm-dd_identificacao.txt	

### Possível erro
Antes de rodar o script faça um SSH do seu terminal para a equipamento, para que o mesmo crie a entrada em <b>/root/.ssh/known_hosts</b> exemplo:
```
# ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 usuario_ssh@172.19.1.1
```

## CRON
```
# crontab -e 
```
Adicione:
```
# Backup Huawei (Todos os dias 20h)
00  20  *   *   *    /root/scripts/BackupHuawei/gerabackup.sh
```
Reinicie o cron:
```
# systemctl restart cron.service
```

### Rotina de limpeza
Adicione ao cron ou script o comando para remover os arquivos mais antigos que 60 dias: 
```
find /home/backups/huawei/* -mtime +60 -exec rm {} \;
```

