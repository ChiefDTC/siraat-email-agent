from load import *
u=load('unsubs.jsonl',('message_id','method'))
print('unsubs 12m',len(u),u.method.value_counts().head(6).to_dict())
sp=load('spam.jsonl',('$flow','$message','Campaign Name'))
print('spam 12m',len(sp))
u90=u[u.ts>=pd.Timestamp('2026-07-09',tz='UTC')]
mm=pd.read_csv('/home/user/siraat-email-agent/baselines/flow-messages-90d.csv')
fm=set(mm.flow_message_id)
u90['src']=np.where(u90.message_id.isin(fm),'flow',np.where(u90.message_id.isna(),'geen bericht','campagne/overig'))
print('unsubs 90d',len(u90),u90.src.value_counts().to_dict())
# weekly unsubs vs sends from account-weekly
aw=pd.read_csv('/home/user/siraat-email-agent/baselines/account-weekly.csv')
print(aw[['week_start_et','unsubscribed_email_marketing_unique','marked_spam_unique']].to_string(index=False))
