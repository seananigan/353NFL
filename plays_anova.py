from scipy import stats
import numpy as np
import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd

NE_NE = []
NE_NFL = []
NFL_NE = []
NFL_NFL = []

#The below appends were copy-pasted from terminal. Pseudo-automation.

NE_NE.append( 0.6872322193658955 )
NE_NFL.append( 0.6639088796962657 )
NFL_NE.append( 0.6795201371036846 )
NFL_NFL.append( 0.700430668102227 )

NE_NE.append( 0.6889460154241646 )
NE_NFL.append( 0.66339887799626 )
NFL_NE.append( 0.6812339331619537 )
NFL_NFL.append( 0.700742335807786 )

NE_NE.append( 0.6855184233076264 )
NE_NFL.append( 0.6634555448518161 )
NFL_NE.append( 0.6820908311910883 )
NFL_NFL.append( 0.7009973366577888 )

NE_NE.append( 0.6923736075407027 )
NE_NFL.append( 0.6638238794129314 )
NFL_NE.append( 0.6778063410454156 )
NFL_NFL.append( 0.7006856689522298 )

NE_NE.append( 0.6863753213367609 )
NE_NFL.append( 0.6641072136907124 )
NFL_NE.append( 0.6803770351328192 )
NFL_NFL.append( 0.7008840029466765 )

NE_NE.append( 0.68808911739503 )
NE_NFL.append( 0.6634555448518161 )
NFL_NE.append( 0.6812339331619537 )
NFL_NFL.append( 0.7004590015300051 )

NE_NE.append( 0.68808911739503 )
NE_NFL.append( 0.6635405451351505 )
NFL_NE.append( 0.6786632390745502 )
NFL_NFL.append( 0.701054003513345 )

NE_NE.append( 0.6812339331619537 )
NE_NFL.append( 0.663427211424038 )
NFL_NE.append( 0.6829477292202228 )
NFL_NFL.append( 0.6990706635688786 )

NE_NE.append( 0.6846615252784919 )
NE_NFL.append( 0.663427211424038 )
NFL_NE.append( 0.6889460154241646 )
NFL_NFL.append( 0.7015923386411288 )

NE_NE.append( 0.689802913453299 )
NE_NFL.append( 0.66280387601292 )
NFL_NE.append( 0.6812339331619537 )
NFL_NFL.append( 0.700742335807786 )

NE_NE.append( 0.6966580976863753 )
NE_NFL.append( 0.664333881112937 )
NFL_NE.append( 0.68808911739503 )
NFL_NFL.append( 0.7000623335411118 )

NE_NE.append( 0.6923736075407027 )
NE_NFL.append( 0.6637672125573751 )
NFL_NE.append( 0.6838046272493573 )
NFL_NFL.append( 0.7002323341077804 )

NE_NE.append( 0.6863753213367609 )
NE_NFL.append( 0.6636822122740409 )
NFL_NE.append( 0.6820908311910883 )
NFL_NFL.append( 0.7000906669688899 )

NE_NE.append( 0.6855184233076264 )
NE_NFL.append( 0.6632288774295915 )
NFL_NE.append( 0.6846615252784919 )
NFL_NFL.append( 0.7003173343911147 )

NE_NE.append( 0.6889460154241646 )
NE_NFL.append( 0.663115543718479 )
NFL_NE.append( 0.6838046272493573 )
NFL_NFL.append( 0.6999206664022214 )

NE_NE.append( 0.6863753213367609 )
NE_NFL.append( 0.6628605428684762 )
NFL_NE.append( 0.6795201371036846 )
NFL_NFL.append( 0.699807332691109 )

NE_NE.append( 0.68808911739503 )
NE_NFL.append( 0.6642205474018247 )
NFL_NE.append( 0.6812339331619537 )
NFL_NFL.append( 0.7004590015300051 )

NE_NE.append( 0.6846615252784919 )
NE_NFL.append( 0.6642205474018247 )
NFL_NE.append( 0.6795201371036846 )
NFL_NFL.append( 0.7000906669688899 )

NE_NE.append( 0.6820908311910883 )
NE_NFL.append( 0.663710545701819 )
NFL_NE.append( 0.6760925449871465 )
NFL_NFL.append( 0.7008556695188984 )

NE_NE.append( 0.6863753213367609 )
NE_NFL.append( 0.6626338754462515 )
NFL_NE.append( 0.6760925449871465 )
NFL_NFL.append( 0.7004873349577831 )

NE_NE.append( 0.6889460154241646 )
NE_NFL.append( 0.6651838839462798 )
NFL_NE.append( 0.6778063410454156 )
NFL_NFL.append( 0.6999773332577776 )

NE_NE.append( 0.6855184233076264 )
NE_NFL.append( 0.6630305434351448 )
NFL_NE.append( 0.6795201371036846 )
NFL_NFL.append( 0.7003740012466708 )

NE_NE.append( 0.6915167095115681 )
NE_NFL.append( 0.664645548818496 )
NFL_NE.append( 0.6846615252784919 )
NFL_NFL.append( 0.700430668102227 )

NE_NE.append( 0.6820908311910883 )
NE_NFL.append( 0.6638238794129314 )
NFL_NE.append( 0.6820908311910883 )
NFL_NFL.append( 0.6997789992633309 )

NE_NE.append( 0.689802913453299 )
NE_NFL.append( 0.663087210290701 )
NFL_NE.append( 0.6812339331619537 )
NFL_NFL.append( 0.700742335807786 )

NE_NE.append( 0.6872322193658955 )
NE_NFL.append( 0.66339887799626 )
NFL_NE.append( 0.6760925449871465 )
NFL_NFL.append( 0.7011673372244575 )

NE_NE.append( 0.6872322193658955 )
NE_NFL.append( 0.662180540601802 )
NFL_NE.append( 0.6820908311910883 )
NFL_NFL.append( 0.6999773332577776 )

NE_NE.append( 0.6872322193658955 )
NE_NFL.append( 0.663710545701819 )
NFL_NE.append( 0.676949443016281 )
NFL_NFL.append( 0.7007706692355641 )

NE_NE.append( 0.6915167095115681 )
NE_NFL.append( 0.6632288774295915 )
NFL_NE.append( 0.6855184233076264 )
NFL_NFL.append( 0.7003456678188927 )

NE_NE.append( 0.6906598114824336 )
NE_NFL.append( 0.6641072136907124 )
NFL_NE.append( 0.6932305055698372 )
NFL_NFL.append( 0.700119000396668 )


normal_NE_NE = stats.normaltest(NE_NE)
normal_NE_NFL = stats.normaltest(NE_NFL)
normal_NFL_NE = stats.normaltest(NFL_NE)
normal_NFL_NFL = stats.normaltest(NFL_NFL)

print("normal_NE_NE:", normal_NE_NE)
print("normal_NE_NFL:", normal_NE_NFL)
print("normal_NFL_NE:", normal_NFL_NE)
print("normal_NFL_NFL:", normal_NFL_NFL)

'''
All but NFL_NE pass the normality test. We fail to reject the null hypothesis
that NE_NE, NE_NFL and NFL_NFL are normal. Even though we reject the null
hypothesis that NFL_NE is normal, we'll proceed with caution anyway.
Judging by the numbers, the means are different anyway, so this next bit
is mainly just to give some formal evidence for that other than the eye test.
'''

anova = stats.f_oneway(NE_NE, NE_NFL, NFL_NE, NFL_NFL)
print(anova)
print("NE_NE mean:", np.mean(NE_NE))
print("NE_NFL mean:", np.mean(NE_NFL))
print("NFL_NE mean:", np.mean(NFL_NE))
print("NFL_NFL mean:", np.mean(NFL_NFL))

data = pd.DataFrame({'NE_NE': NE_NE, 'NE_NFL': NE_NFL, 'NFL_NE': NFL_NE, 'NFL_NFL': NFL_NFL})
# print(data)
data_melt = pd.melt(data)
posthoc = pairwise_tukeyhsd(data_melt['value'], data_melt['variable'], alpha=0.05)
print(posthoc)