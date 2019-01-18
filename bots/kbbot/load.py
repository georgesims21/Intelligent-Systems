from .kb import KB, Boolean, Integer

# Define our propositional symbols
# J1 is true if the card with index 1 is a jack, etc
# You need to initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.

# -- play jacks -- #
J0 = Boolean('j0')
J1 = Boolean('j1')
J2 = Boolean('j2')
J3 = Boolean('j3')
J4 = Boolean('j4')
J5 = Boolean('j5')
J6 = Boolean('j6')
J7 = Boolean('j7')
J8 = Boolean('j8')
J9 = Boolean('j9')
J10 = Boolean('j10')
J11 = Boolean('j11')
J12 = Boolean('j12')
J13 = Boolean('j13')
J14 = Boolean('j14')
J15 = Boolean('j15')
J16 = Boolean('j16')
J17 = Boolean('j17')
J18 = Boolean('j18')
J19 = Boolean('j19')

# -- play queen -- #
Q0 = Boolean('q0')
Q1 = Boolean('q1')
Q2 = Boolean('q2')
Q3 = Boolean('q3')
Q4 = Boolean('q4')
Q5 = Boolean('q5')
Q6 = Boolean('q6')
Q7 = Boolean('q7')
Q8 = Boolean('q8')
Q9 = Boolean('q9')
Q10 = Boolean('q10')
Q11 = Boolean('q11')
Q12 = Boolean('q12')
Q13 = Boolean('q13')
Q14 = Boolean('q14')
Q15 = Boolean('q15')
Q16 = Boolean('q16')
Q17 = Boolean('q17')
Q18 = Boolean('q18')
Q19 = Boolean('q19')

# -- play kings -- #
K0 = Boolean('k0')
K1 = Boolean('k1')
K2 = Boolean('k2')
K3 = Boolean('k3')
K4 = Boolean('k4')
K5 = Boolean('k5')
K6 = Boolean('k6')
K7 = Boolean('k7')
K8 = Boolean('k8')
K9 = Boolean('k9')
K10 = Boolean('k10')
K11 = Boolean('k11')
K12 = Boolean('k12')
K13 = Boolean('k13')
K14 = Boolean('k14')
K15 = Boolean('k15')
K16 = Boolean('k16')
K17 = Boolean('k17')
K18 = Boolean('k18')
K19 = Boolean('k19')

# -- play tens -- #
T0 = Boolean('t0')
T1 = Boolean('t1')
T2 = Boolean('t2')
T3 = Boolean('t3')
T4 = Boolean('t4')
T5 = Boolean('t5')
T6 = Boolean('t6')
T7 = Boolean('t7')
T8 = Boolean('t8')
T9 = Boolean('t9')
T10 = Boolean('t10')
T11 = Boolean('t11')
T12 = Boolean('t12')
T13 = Boolean('t13')
T14 = Boolean('t14')
T15 = Boolean('t15')
T16 = Boolean('t16')
T17 = Boolean('t17')
T18 = Boolean('t18')
T19 = Boolean('t19')

# -- play aces --#
A0 = Boolean('a0')
A1 = Boolean('a1')
A2 = Boolean('a2')
A3 = Boolean('a3')
A4 = Boolean('a4')
A5 = Boolean('a5')
A6 = Boolean('a6')
A7 = Boolean('a7')
A8 = Boolean('a8')
A9 = Boolean('a9')
A10 = Boolean('a10')
A11 = Boolean('a11')
A12 = Boolean('a12')
A13 = Boolean('a13')
A14 = Boolean('a14')
A15 = Boolean('a15')
A16 = Boolean('a16')
A17 = Boolean('a17')
A18 = Boolean('a18')
A19 = Boolean('a19')

P0 = Boolean('p0')
P1 = Boolean('p1')
P2 = Boolean('p2')
P3 = Boolean('p3')
P4 = Boolean('p4')
P5 = Boolean('p5')
P6 = Boolean('p6')
P7 = Boolean('p7')
P8 = Boolean('p8')
P9 = Boolean('p9')
P10 = Boolean('p10')
P11 = Boolean('p11')
P12 = Boolean('p12')
P13 = Boolean('p13')
P14 = Boolean('p14')
P15 = Boolean('p15')
P16 = Boolean('p16')
P17 = Boolean('p17')
P18 = Boolean('p18')
P19 = Boolean('p19')

# -- singular cards -- #
AC = Boolean('ac')
TC = Boolean('tc')
KC = Boolean('kc')
QC = Boolean('qc')
JC = Boolean('jc')
AD = Boolean('ad')
TD = Boolean('td')
KD = Boolean('kd')
QD = Boolean('qd')
JD = Boolean('jd')
AH = Boolean('ah')
TH = Boolean('th')
KH = Boolean('kh')
QH = Boolean('qh')
JH = Boolean('jh')
AS = Boolean('as')
TS = Boolean('ts')
KS = Boolean('ks')
QS = Boolean('qs')
JS = Boolean('js')

PAC = Boolean('pac')
PTC = Boolean('ptc')
PKC = Boolean('pkc')
PQC = Boolean('pqc')
PJC = Boolean('pjc')
PAD = Boolean('pad')
PTD = Boolean('ptd')
PKD = Boolean('pkd')
PQD = Boolean('pqd')
PJD = Boolean('pjd')
PAH = Boolean('pah')
PTH = Boolean('pth')
PKH = Boolean('pkh')
PQH = Boolean('pqh')
PJH = Boolean('pjh')
PAS = Boolean('pas')
PTS = Boolean('pts')
PKS = Boolean('pks')
PQS = Boolean('pqs')
PJS = Boolean('pjs')


def jacks_information(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    # This adds information which cards are Jacks
    kb.add_clause(J4)
    kb.add_clause(J9)
    kb.add_clause(J14)
    kb.add_clause(J19)
    # Add here whatever is needed for your strategy.

def jacks_knowledge(kb):
    # DEFINITION OF THE STRATEGY
    # Add clauses (This list is sufficient for this strategy)
    # PJ is the strategy to play jacks first, so all we need to model is all x PJ(x) <-> J(x),
    # In other words that the PJ strategy should play a card when it is a jack
    kb.add_clause(~J4, P4)
    kb.add_clause(~J9, P9)
    kb.add_clause(~J14, P14)
    kb.add_clause(~J19, P19)
    kb.add_clause(~P4, J4)
    kb.add_clause(~P9, J9)
    kb.add_clause(~P14, J14)
    kb.add_clause(~P19, J19)

def aces_information(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    # This adds information which cards are Jacks
    kb.add_clause(A0)
    kb.add_clause(A5)
    kb.add_clause(A10)
    kb.add_clause(A15)
    # Add here whatever is needed for your strategy.

def aces_knowledge(kb):
    # DEFINITION OF THE STRATEGY
    # Will play an ace if there is one in the hand 
    kb.add_clause(~A0, P0)
    kb.add_clause(~A5, P5)
    kb.add_clause(~A10, P10)
    kb.add_clause(~A15, P15)
    kb.add_clause(~P0, A0)
    kb.add_clause(~P5, A5)
    kb.add_clause(~P10, A10)
    kb.add_clause(~P15, A15)

def cheap_information(kb):
    # GENERAL INFORMATION ABOUT THE CARDS
    # This adds information which cards are Jacks
    kb.add_clause(J4)
    kb.add_clause(J9)
    kb.add_clause(J14)
    kb.add_clause(J19)

    # This adds information which cards are Queens
    kb.add_clause(Q3)
    kb.add_clause(Q8)
    kb.add_clause(Q13)
    kb.add_clause(Q18)

    # This adds information which cards are Kings
    kb.add_clause(K2)
    kb.add_clause(K7)
    kb.add_clause(K12)
    kb.add_clause(K17)

def cheap_knowledge(kb):
    # DEFINITION OF THE STRATEGY
    # Play a cheap card (J < Q < K)

    kb.add_clause(~J4, P4)
    kb.add_clause(~J9, P9)
    kb.add_clause(~J14, P14)
    kb.add_clause(~J19, P19)
    kb.add_clause(~P4, J4)
    kb.add_clause(~P9, J9)
    kb.add_clause(~P14, J14)
    kb.add_clause(~P19, J19)

    kb.add_clause(~Q3, P3)
    kb.add_clause(~Q8, P8)
    kb.add_clause(~Q13, P13)
    kb.add_clause(~Q18, P18)
    kb.add_clause(~P3, Q3)
    kb.add_clause(~P8, Q8)
    kb.add_clause(~P13, Q13)
    kb.add_clause(~P18, Q18)

    kb.add_clause(~K2, P2)
    kb.add_clause(~K7, P7)
    kb.add_clause(~K12, P12)
    kb.add_clause(~K17, P17)
    kb.add_clause(~P2, K2)
    kb.add_clause(~P7, K7)
    kb.add_clause(~P12, K12)
    kb.add_clause(~P17, K17)

