import maya.cmds as mc
import math as math
# this is 100% made and copyrighted by korean SANG BIN LEE
# I'm finding a job now(2022/07). Rigging TA / CFX Artist / Character TD is good for me.
# my github : https://github.com/SANG-BIN-LEE
# my linkedin : https://www.linkedin.com/in/sangbin-lee-981a7215a
# my youtube : https://www.youtube.com/playlist?list=PLKIoBfXktlaalLuyrsqxT3QgzhQ-08yeE
# maintenance work is needed, yet.

class BinController():
    def __init__(self):
        pass
    def circle_CTL(self, n = 'circle_CTL', s=1, c=None):
        k = mc.circle(c = (0,0,0), nr=(1,0,0), n=n, r=s)
        if c:
            shape = mc.listRelatives(k, c=1)[0]
            mc.setAttr(shape+'.overrideEnabled', 1)
            mc.setAttr(shape+'.overrideColor', c)
        mc.delete(mc.listConnections(mc.listRelatives(k, s=1), s=1, d=0))
        return n
    def cube_CTL(self, n = 'cube_CTL', s=1, c=None):
        k = mc.curve(d=1, p =[(0.5*s, 0.5*s, 0.5*s), (0.5*s, 0.5*s, -0.5*s), (-0.5*s, 0.5*s, -0.5*s), (-0.5*s, -0.5*s, -0.5*s), (0.5*s, -0.5*s, -0.5*s), (0.5*s, 0.5*s, -0.5*s), (-0.5*s, 0.5*s, -0.5*s), (-0.5*s, 0.5*s, 0.5*s), (0.5*s, 0.5*s, 0.5*s), (0.5*s, -0.5*s, 0.5*s), (0.5*s, -0.5*s, -0.5*s), (-0.5*s, -0.5*s, -0.5*s), (-0.5*s, -0.5*s, 0.5*s), (0.5*s, -0.5*s, 0.5*s), (-0.5*s, -0.5*s, 0.5*s), (-0.5*s, 0.5*s, 0.5*s)], n= n)
        if c:
            shape = mc.listRelatives(k, s=1)[0]
            mc.setAttr(shape+'.overrideEnabled', 1)
            mc.setAttr(shape+'.overrideColor', c)
        return n
    def dia_CTL(self, n = 'dia_CTL', s=1, c=None):
        k = mc.curve(d=1, p = [(0.0*s, 1.0*s, 0.0*s), (1.0*s, 0.0*s, 0.0*s), (0.0*s, 0.0*s, 1.0*s), (-1.0*s, 0.0*s, 0.0*s), (0.0*s, 0.0*s, -1.0*s), (0.0*s, 1.0*s, 0.0*s), (0.0*s, 0.0*s, 1.0*s), (0.0*s, -1.0*s, 0.0*s), (0.0*s, 0.0*s, -1.0*s), (1.0*s, 0.0*s, 0.0*s), (0.0*s, 1.0*s, 0.0*s), (-1.0*s, 0.0*s, 0.0*s), (0.0, -1.0*s, 0.0), (1.0*s, 0.0, 0.0)], n= n)
        if c:
            shape = mc.listRelatives(k, s=1)[0]
            mc.setAttr(shape+'.overrideEnabled', 1)
            mc.setAttr(shape+'.overrideColor', c)
        return n
    def halfdia_CTL(self, n = 'halfdia_CTL', s=1, c=None):
        k = mc.curve(d=1, p = [(0.0, 1.0*s, -2.0), (1.0*s, 0.0, -2.0*s), (0.0, 0.0, 0.0), (-1.0*s, 0.0, -2.0*s), (0.0, 1.0*s, -2.0), (0.0, 0.0, 0.0), (0.0, -1.0*s, -2.0*s), (1.0*s, 0.0, -2.0*s), (0.0, 1.0*s, -2.0*s), (-1.0*s, 0.0, -2.0*s), (0.0, -1.0*s, -2.0*s), (1.0*s, 0.0, -2.0*s)], n= n)
        if c:
            shape = mc.listRelatives(k, s=1)[0]
            mc.setAttr(shape+'.overrideEnabled', 1)
            mc.setAttr(shape+'.overrideColor', c)
        return n
    def hand_CTL(self, n = 'hand_CTL', s=1, c=None):
        k = mc.curve(d=2, p = [(0.0, 0.0, 1.2244654084165918*s), (2.0707746269703278*s, 0.0, 2.520293241046993*s), (3.68036774110874*s, 0.0, 3.261048364647314*s), (4.364444814617565*s, 0.0, 3.199009378967995*s), (4.4449244703244855*s, 0.0, 2.6406585078541265*s), (3.2779694625741365*s, 0.0, 1.6480347369850294*s), (2.9962906675999155*s, 0.0, 1.4929372727867336*s), (5.611879478074834*s, 0.0, 1.3998787942677546*s), (7.664110698601311*s, 0.0, 1.3688593014280965*s), (8.348187772110133*s, 0.0, 0.872547415993548*s), (7.784830182161691*s, 0.0, 0.46929400907797647*s), (5.491159994514454*s, 0.0, 0.6243914732762732*s), (3.3182092904275966*s, 0.0, 0.5623524875969553*s), (3.1170101511602955*s, 0.0, 0.5313329947572948*s), (3.3182092904275966*s, 0.0, 0.43827451623831687*s), (5.410680338807533*s, 0.0, 0.3141965448796795*s), (7.543391215040929*s, 0.0, 0.221138066360702*s), (8.146988632842834*s, 0.0, -0.02701787635657318*s), (8.348187772110137*s, 0.0, -0.5543492546307814*s), (7.583631042894389*s, 0.0, -0.7714857045083954*s), (4.726603265298708*s, 0.0, -0.6163882403100996*s), (3.197489806867216*s, 0.0, -0.4923102689514624*s), (2.996290667599915*s, 0.0, -0.6163882403100996*s), (3.2779694625741365*s, 0.0, -0.7094467188290775*s), (4.766843093152168*s, 0.0, -0.926583168706692*s), (7.583631042894389*s, 0.0, -0.9576026615463522*s), (8.348187772110137*s, 0.0, -1.1437196185843084*s), (8.307947944256675*s, 0.0, -1.7020704896981735*s), (7.503151387187469*s, 0.0, -2.043284910934425*s), (4.565643953884866*s, 0.0, -1.857167953896472*s), (3.0767703233068353*s, 0.0, -1.7330899825378336*s), (2.8755711840395346*s, 0.0, -1.7951289682171514*s), (3.3182092904275966*s, 0.0, -1.91920693957579*s), (4.4449244703244855*s, 0.0, -1.981245925255108*s), (7.221472592213248*s, 0.0, -2.353479839331021*s), (7.422671731480548*s, 0.0, -2.694694260567273*s), (6.778834485825185*s, 0.0, -3.159986653162164*s), (5.410680338807533*s, 0.0, -3.0359086818035244*s), (1.8293356598495665*s, 0.0, -2.574408712561952*s), (0.0, 0.0, -1.4729664211276916*s)], n= n)
        if c:
            shape = mc.listRelatives(k, s=1)[0]
            mc.setAttr(shape+'.overrideEnabled', 1)
            mc.setAttr(shape+'.overrideColor', c)
        return n            
    def loc_CTL(self, n = 'loc_CTL', s=1, c=None):
        k = mc.curve(d=1, p = [(-1.0*s, 0.0, 0.0), (1.0*s, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 1.0*s), (0.0, 0.0, -1.0*s), (0.0, 0.0, 0.0), (0.0, 1.0*s, 0.0), (0.0, -1.0*s, 0.0)], n= n)
        if c:
            shape = mc.listRelatives(k, s=1)[0]
            mc.setAttr(shape+'.overrideEnabled', 1)
            mc.setAttr(shape+'.overrideColor', c)
        return n
    def circleFront_CTL(self, n = 'circleFront_CTL', s=1, d=1, c=None):
        k = mc.circle(c = (d,0,0), nr=(1,0,0), n=n, r=s)
        if c:
            shape = mc.listRelatives(k, c=1)[0]
            mc.setAttr(shape+'.overrideEnabled', 1)
            mc.setAttr(shape+'.overrideColor', c)
        mc.delete(mc.listConnections(mc.listRelatives(k, s=1), s=1, d=0))
        return n
    def help(self):
        print("""
        circle_CTL(n=name, s=scale, c=color)
        circleFront_CTL(n=name, s=scale, c=color, d=distance)
        cube_CTL(n=name, s=scale, c=color)
        dia_CTL(n=name, s=scale, c=color)
        loc_CTL(n=name, s=scale, c=color)
        all returns name
        """)

class BinIKSetting():
    def __init__(self):
        pass
    def ikPVT(self, ikList=mc.ls(sl=1, type='joint')):
        self.ikList = ikList
        if not len(self.ikList) == 3:
            mc.error('please select 3 joint.')
            return
        ikRoot, ikMiddle, ikTip = self.ikList

        #calculate pos
        space1 = mc.xform (ikRoot, q=1, ws=1, t=1)
        space2 = mc.xform (ikMiddle, q=1, ws=1, t=1)
        space3 = mc.xform (ikTip, q=1, ws=1, t=1)
        x1,y1,z1 = space1
        x2,y2,z2 = space2
        x3,y3,z3 = space3
        
        #calculate PV
        #ua dot product
        ua = (x3-x1)*(x3-x2)+(y3-y1)*(y3-y2)+(z3-z1)*(z3-z2)
        u = math.sqrt((x3-x1)**2+(y3-y1)**2+(z3-z1)**2)
        d = ua/u
        uVec = ((x3-x1),(y3-y1),(z3-z1))
        mx,my,mz = ((x3-x1)*(u-d)/u, (y3-y1)*(u-d)/u, (z3-z1)*(u-d)/u)
        pos1 = ((x1+mx),(y1+my),(z1+mz))
        self.poseH = pos1
        x4,y4,z4 = pos1
        a = math.sqrt((x3-x2)**2+(y3-y2)**2+(z3-z2)**2)
        h = math.sqrt(a**2 - d**2)
        hVec = ((x2-x4),(y2-y4),(z2-z4))
        #uh vector product
        UH = (uVec[1]*hVec[2]-uVec[2]*hVec[1], uVec[2]*hVec[0]-uVec[0]*hVec[2], uVec[0]*hVec[1]-uVec[1]*hVec[0])
        #uh length
        uh = math.sqrt(UH[0]**2+UH[1]**2+UH[2]**2)
        
        posPV = (pos1[0]+3*hVec[0], pos1[1]+3*hVec[1], pos1[2]+3*hVec[2])

        X = [uVec[0]/u, uVec[1]/u, uVec[2]/u, 0]
        Y = [UH[0]/uh, UH[1]/uh, UH[2]/uh, 0]
        Z = [-hVec[0]/h, -hVec[1]/h, -hVec[2]/h, 0]
        T = [posPV[0], posPV[1], posPV[2], 1]
        PVmt = []
        for x in X:
            PVmt.append(x)
        for y in Y:
            PVmt.append(y)
        for z in Z:
            PVmt.append(z)
        for t in T:
            PVmt.append(t)
        self.PVmt = PVmt
        self.posPV = posPV

        return posPV
    def ikRPSet(self, n='name', s=5, aim=(1,0,0)):
        if not len(self.ikList) == 3:
            mc.error('please select 3 joint.')
            return

        ikRoot, ikMiddle, ikTip = self.ikList

        #createController_Hand
        mc.select(cl=1)
        Tipmaster = mc.group(em=1, n=n+'_MCTL')
        Tipmain = BinCTL.cube_CTL(n=n+'_CTL', s=s*1.2, c=17)
        mc.setAttr(Tipmain+'.v', lock=1, keyable=0, cb=0)
        mc.setAttr(Tipmain+'.sx', lock=1, keyable=0, cb=0)
        mc.setAttr(Tipmain+'.sy', lock=1, keyable=0, cb=0)
        mc.setAttr(Tipmain+'.sz', lock=1, keyable=0, cb=0)
        Tipnull = BinCTL.cube_CTL(n=n+'_n_CTL', s =s*1, c=21)
        mc.setAttr(Tipnull+'.v', lock=1, keyable=0, cb=0)
        mc.setAttr(Tipnull+'.sx', lock=1, keyable=0, cb=0)
        mc.setAttr(Tipnull+'.sy', lock=1, keyable=0, cb=0)
        mc.setAttr(Tipnull+'.sz', lock=1, keyable=0, cb=0)
        mc.parent(Tipnull,Tipmain)
        mc.parent(Tipmain,Tipmaster)
        ro = mc.getAttr(ikTip+'.rotateOrder')
        mc.setAttr(Tipmaster+'.rotateOrder', ro)
        mc.setAttr(Tipmain+'.rotateOrder', ro)
        mc.setAttr(Tipnull+'.rotateOrder', ro)
        mc.matchTransform(Tipmaster, ikTip)

        #createController_PV
        mc.select(cl=1)
        PVmaster = mc.group(em=1, n=n+'_MPVCTL')
        PVmain = BinCTL.halfdia_CTL(n=n+'_PV_CTL', s=s*0.5, c=17)
        mc.setAttr(PVmain+'.v', lock=1, keyable=0, cb=0)
        mc.setAttr(PVmain+'.sx', lock=1, keyable=0, cb=0)
        mc.setAttr(PVmain+'.sy', lock=1, keyable=0, cb=0)
        mc.setAttr(PVmain+'.sz', lock=1, keyable=0, cb=0)
        mc.setAttr(PVmain+'.rx', lock=1, keyable=0, cb=0)
        mc.setAttr(PVmain+'.ry', lock=1, keyable=0, cb=0)
        mc.setAttr(PVmain+'.rz', lock=1, keyable=0, cb=0)
        mc.parent(PVmain, PVmaster)
        mc.setAttr(PVmaster+'.offsetParentMatrix', self.PVmt, type='matrix')

        RP = mc.ikHandle(sol='ikRPsolver', n=n+'_ikRPsolver', sj=ikRoot, ee=ikTip)
        RPsolver = RP[0]
        mc.rename(RP[1], n+'_ikRPee')
        mc.parent(RPsolver, Tipnull)
        mc.poleVectorConstraint(PVmain, RPsolver)
        dMt = mc.createNode('decomposeMatrix', n='IKdMt_'+ikTip)
        lR = mc.listRelatives(ikTip, p=1)[0] or ''
        if not lR == '':
            multMt = mc.createNode('multMatrix', n='multMt'+ikTip)
            mc.connectAttr(Tipnull+'.worldMatrix', multMt+'.matrixIn[0]')
            mc.connectAttr(lR+'.worldInverseMatrix', multMt+'.matrixIn[1]')
            mc.connectAttr(multMt+'.matrixSum', dMt+'.inputMatrix')
        else:
            mc.connectAttr(Tipnull+'.worldMatrix', dMt+'.inputMatrix')
        mc.connectAttr(dMt+'.outputRotate', ikTip+'.jointOrient')

        self.RPsolver = RPsolver
        self.Tipmain = Tipmain
        self.Tipnull = Tipnull
        self.PVmain = PVmain
        return RPsolver, Tipmain, Tipnull, PVmain
    def ikSpline(self, j = mc.ls(sl=1, type='joint'), d=3, n = 'spline'):
        self.splineJoint = j
        ev = []
        for x in self.Joint:
            point = mc.xform(x,q=1,ws=1,t=1)
            ev.append(tuple(point))
        mc.select(cl=1)
        mc.curve(d=3, ep=ev, n=n+'_ikCurve')
        mc.ikHandle(sj=self.Joint[0], ee=self.Joint[-1], c=n+'_ikCurve', n=n+'_ikHandle', sol='ikSplineSolver', ccv=0, scv=0, pcv=0)
    def help(self):
        print("""
        ikPVT(ikList = mc.ls(sl=1))
        ikRPSet(n=stringName, s=3 scale) -needed PVT first, color is fixed
        ikSpline(j=joints, d=3 degree, n=name)
        """ )

class BinFKSetting():
    def __init__(self):
        pass
    def BinFK(self, fkList=mc.ls(sl=1, type='joint'), M=True, MS=False, N=False, NS=False, s=10, c=18):
        self.fkList = fkList
        
        c_grp_p = {}
        c_grp_c = {}
        c_grp_shape = {}
        c_CTL= {}
        
        # controller make
        for x in self.fkList:

            # Naming Basic
            if '_joint' in x:
                y=x.replace('_joint','')
            elif '_JNT' in x:
                y=x.replace('_JNT','')
            else:
                y=x
                        
            # CTL Create
            CTL = BinCTL.circle_CTL(n=y+'_CTL', c=c, s=s)
            mc.setAttr(CTL+'.v', lock=1, keyable=0, cb=0)
            c_CTL[x] = CTL
            
            # Master Control Create
            if M==True:
                if MS==True:
                    m_CTL = BinCTL.circle_CTL(n=y+'_m_CTL', c=1, s=s*1.2)
                    mc.setAttr(m_CTL+'.v', lock=1, keyable=0, cb=0)
                else:
                    m_CTL = mc.group(em=1, n=y+'_MCTL')
            
            # Null Control Create
            if N == True:
                if NS ==True:
                    n_CTL = BinCTL.circle_CTL(n=y+'_n_CTL', c=3, s=s*0.8)
                    mc.setAttr(n_CTL+'.v', lock=1, keyable=0, cb=0)
                else:
                    n_CTL = mc.group(em=1, n=y+'_NCTL')

            # Control Parent, Constraint
            if M==True:
                mc.parent(CTL, m_CTL)
                c_grp_p[x] = m_CTL

                if N==True:
                    mc.parent(n_CTL, CTL)
                    c_grp_c[x] = n_CTL
                else:
                    c_grp_c[x] = CTL

            else:
                c_grp_p[x] = CTL
                if N==True:
                    mc.parent(n_CTL, CTL)
                    c_grp_c[x] = n_CTL
                else:
                    c_grp_c[x] = CTL
        
        for x in self.fkList:
            # controller rotationOrder / Constraint
            ro = mc.getAttr(x+'.rotateOrder')
            mc.setAttr(c_CTL[x]+'.rotateOrder', ro)
            mc.setAttr(c_grp_c[x]+'.rotateOrder', ro)
            mc.setAttr(c_grp_p[x]+'.rotateOrder', ro)
            mc.matchTransform(c_grp_p[x], x)
            dMt = mc.createNode('decomposeMatrix', n='FKdMt_'+x)
            pMt = mc.createNode('pickMatrix', n='FKpMt_'+x)
            lR = mc.listRelatives(x, p=1)[0] or ''
            if not lR == '':
                multMt = mc.createNode('multMatrix', n='multMt'+x)
                mc.connectAttr(c_grp_c[x]+'.worldMatrix', multMt+'.matrixIn[0]')
                mc.connectAttr(lR+'.worldInverseMatrix', multMt+'.matrixIn[1]')
                mc.connectAttr(multMt+'.matrixSum', pMt+'.inputMatrix')
            else:
                mc.connectAttr(c_grp_c[x]+'.worldMatrix', pMt+'.inputMatrix')
            mc.connectAttr(pMt+'.outputMatrix', dMt+'.inputMatrix')
            mc.connectAttr(dMt+'.outputTranslate', x+'.t')
            mc.connectAttr(dMt+'.outputRotate', x+'.jointOrient')
            mc.connectAttr(dMt+'.outputScale', x+'.s')

            # controller Parent
            children = mc.listRelatives(x, c=1, type='joint', path=1) or []
            if not children == []:
                for child in children:
                    childname = child.split('|')[-1]
                    mc.parent(c_grp_p[childname], c_grp_c[x])
    def BinHand(self, thumbList, indexList, middleList, ringList, pinkyList):
        pass
    def help(self):
        print("""
        BinFK : fkList = jointList, M=master, MS=MasterShape, N=null, NS=NullShape, s=controllerscale, c=color
        """)

class BinIKFKSwitch():
    def __init__(self):
        pass
    def FKtoIK(self, FKJoints, PV_CTL, IKRP_CTL):
        tx, ty, tz = BinIK.ikPVT(ikList=FKJoints)
        mc.setAttr(PV_CTL+'.tx', tx)
        mc.setAttr(PV_CTL+'.ty', ty)
        mc.setAttr(PV_CTL+'.tz', tz)
        mc.matchTransform(IKRP_CTL, FKJoints[3])
    def IKtoFK(self, IKJoints, FK_CTLs):
        mc.matchTransform(FK_CTLs[0], IKJoints[0])
        mc.matchTransform(FK_CTLs[1], IKJoints[1])
        mc.matchTransform(FK_CTLs[2], IKJoints[2])
    def help(self):
        print("""
        FKtoIK = FKJoints, PV_CTL, IKRP_CTL
        IKtoFK = IKJoints, FK_CTLs
        """)

class BinJoint():
    def __init__(self):
        pass
    def duplicate(self, j=mc.ls(sl=1,type='joint'), pre='', suf='', org='', mod=''):
        if j == []:
            mc.error('please select one joint')
            return
        #list Hierarchy
        mc.select(j, hi=1)
        Joints = mc.ls(sl=1,type='joint')
        mc.select(cl=1)

        #save ParentTree
        child = Joints
        Pa = {}
        for x in range(len(child)):
            PA = mc.listRelatives(child[x], p=1)
            if PA:
                C = child[x]
                c = pre+C.replace(org,mod)+suf
                P = PA[0]
                p = pre+P.replace(org,mod)+suf
                Pa[c] = p
        child = Pa.keys()

        #duplicate
        for x in Joints:
            k = pre+x.replace(org,mod)+suf
            mc.duplicate(x, po=1, n=k)
            try:
                mc.parent(k, w=1)
            except:
                pass
        
        #set ParentTree
        for x in child:
            if Pa[x]:
                mc.parent(x, Pa[x])
    def MirrorYZ(self, j=mc.ls(sl=1, type='joint'), org='_l', mod='_r', flip = True, xflip = True):
        if j == []:
            mc.error('please select joint')
            return
        
        #list Hierarchy
        mc.select(j, hi=1)
        Joints = mc.ls(sl=1,type='joint')
        mc.select(cl=1)

        #save ParentTree
        child = Joints
        Pa = {}
        for x in range(len(child)):
            PA = mc.listRelatives(child[x], p=1)
            if PA:
                C = child[x]
                c = C.replace(org,mod)
                P = PA[0]
                p = P.replace(org, mod)
                Pa[c] = p
        child = Pa.keys()
        
        #duplicate
        for x in Joints:
            k = x.replace(org, mod)
            mc.duplicate(x, po=1, n=k)
            try:
                mc.parent(k, w=1)
            except:
                pass

            #set trans, orient
            mt = mc.getAttr(k+'.worldMatrix')
            if flip == True:
                vx1 = mt[0]
                tx = mt[12]
                vy1 = mt[4]
                vy2 = mt[5]
                vy3 = mt[6]
                vz1 = mt[8]
                vz2 = mt[9]
                vz3 = mt[10]
                mt[0] = -1*vx1
                mt[12] = -1*tx
                mt[4] = -1*vy1
                mt[5] = -1*vy2
                mt[6] = -1*vy3
                mt[8] = -1*vz1
                mt[9] = -1*vz2
                mt[10] = -1*vz3
            if flip == False:
                vx1 = mt[0]
                tx = mt[12]
                mt[0] = -1*vx1
                mt[12] = -1*tx
            if xflip == False:
                mt[0] = vx1
                
            mc.createNode('decomposeMatrix', n='temp')
            mc.setAttr('temp.inputMatrix', mt, type='matrix')
            T = mc.getAttr('temp.outputTranslate')[0]
            mc.setAttr(k+'.tx', T[0])
            mc.setAttr(k+'.ty', T[1])
            mc.setAttr(k+'.tz', T[2])
            R = mc.getAttr('temp.outputRotate')[0]
            mc.setAttr(k+'.jointOrientX', R[0])
            mc.setAttr(k+'.jointOrientY', R[1])
            mc.setAttr(k+'.jointOrientZ', R[2])
            mc.delete('temp')

        #set ParentTree
        for x in child:
            if Pa[x]:
                mc.parent(x, Pa[x])
    def help(self):
        print("""
        def duplicate(self, j=mc.ls(sl=1,type='joint'), pre='', suf='', org='', mod='')
        MirrorYZ(self, j=mc.ls(sl=1, type='joint'), org='_l', mod='_r', flip = True)    
        """)
