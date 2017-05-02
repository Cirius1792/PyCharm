from TDP.Progetto1.pkg_1.TwoDTreeMap_new import TwoDTreeMap
from TDP import util

if __name__ == '__main__':
    print("\n\n----------------------------------------------------------------")
    print('----------- Gruppo #10 - Test Albero (2,d) ---------------------')
    print("----------------------------------------------------------------")

    print('\n------------ Test Albero (2, 4) ---------------------')
    pTree = TwoDTreeMap()

    dic = util.rand_dict(30, 1, 100)
    for k in dic:
        pTree[k] = dic.get(k)


    print('\n---- Albero (2, 4)  ----')
    pTree.display_tree()
    print(len(pTree))

    print('\n---- Cancellazione di tutti gli elementi  ----')
    for k in dic:
        del pTree[k]
        print('\n### Cancellazione di ', k, '###')
        pTree.display_tree()
        print(len(pTree))
        print('############################')

    print('\n------------ Test Albero (2, 6) ---------------------')
    pTree = TwoDTreeMap(6)

    dic = util.rand_dict(30, 1, 100)
    for k in dic:
        pTree[k] = dic.get(k)

    print('\n---- Albero (2, 6)  ----')
    pTree.display_tree()

    print('\n---- Cancellazione di tutti gli elementi  ----')
    for k in dic:
        del pTree[k]
        print('\n### Cancellazione di ', k, '###')
        pTree.display_tree()
        print('############################')




