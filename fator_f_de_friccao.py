import numpy as np

class Questao3():
    
    def __init__(self):
        self.re = 0
        self.f = 0
        self.cont_it = 0
    
    def __funcaoG(self,re,f):
        func = 4*(np.log10(re*(f**0.5)))-0.4-((1)/(f**0.5))
        return func
    
    def __error_e(self,f_inf,f_sup):
        __error_e = np.absolute((f_inf - f_sup)/(f_inf))*100
        return __error_e

    def __raiz_bisseccao(self,itera,f_inf,f_sup,re):
        
        func_inf = self.__funcaoG(re,f_inf)
        func_sup = self.__funcaoG(re,f_sup)
        n = 0
        if func_inf == 0:
            return f_inf
        if func_sup == 0:
            return f_sup
        elif func_inf * func_sup < 0:
            erro_e = self.__error_e(f_inf,f_sup)
            f1 = f_inf
            f_1 = f_sup
            while n <= itera:
                n = n + 1
                f_novo = (f1+f_1)/2
                if self.__funcaoG(re,f1) * self.__funcaoG(re,f_novo) < 0 and self.__funcaoG(re,f_1) * self.__funcaoG(re,f_novo) > 0:
                    if self.__funcaoG(re,f1) > 0 and self.__funcaoG(re,f_1) < 0:
                        f_1 = f_novo
                        erro_e = self.__error_e(f_inf,f_sup)
                    elif self.__funcaoG(re,f1) < 0 and self.__funcaoG(re,f_1) > 0:
                        f_1 = f_novo
                        erro_e = self.__error_e(f_inf,f_sup)
                elif self.__funcaoG(re,f_1) * self.__funcaoG(re,f_novo) < 0 and self.__funcaoG(re,f1) * self.__funcaoG(re,f_novo)> 0:
                    if self.__funcaoG(re,f_1) > 0 and self.__funcaoG(re,f1) < 0:
                        f1 = f_novo
                        erro_e = self.__error_e(f_inf,f_sup)
                    elif self.__funcaoG(re,f_1) < 0 and self.__funcaoG(re,f1) > 0:
                        f1 = f_novo
                        erro_e = self.__error_e(f_inf,f_sup)
                self.cont_it = self.cont_it + 1
            self.f = (f1 + f_1)/2
            return (f1 + f_1)/2
    
    def resultado_bisseccao(self,itera,f_inf,f_sup,re):
        a = self.__raiz_bisseccao(itera,f_inf,f_sup,re)
        print('-------------------------------------------------------')
        print('Resultados da simulação usando o método da bissecção:')
        print('Fator f: '+str(a)+';')
        print('Número de iterações realizadas: '+str(self.cont_it)+'.')
        print('-------------------------------------------------------')
       
itera = 4
f_inf = 0.01
f_sup = 0.02
re = 2000
obj = Questao3()
obj.resultado_bisseccao(itera,f_inf,f_sup,re)