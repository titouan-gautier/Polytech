class B extends A {

    int i ;

    A a ;

    B(int _i, A _a){ i=_i ; a = _a ;}

    int m (){ return 1 + a.m() ; }
}
