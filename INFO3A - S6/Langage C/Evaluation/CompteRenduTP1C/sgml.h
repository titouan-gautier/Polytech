#include "pile.h"

enum ETagEtat {
	NoTag,
	Opening, /*tag ouvrante*/
	Closing /*tag fermante*/
};

int TagSGML(FILE *fp);

int VerifImbrication(char *tg,enum ETagEtat *tgE,struct SPile *p);
