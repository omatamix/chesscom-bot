#ifndef DEPS_H
#define DEPS_H

typedef unsigned long long U160;

#define NAME "Firestorm"
#define BRD_SQ_NUM 288

#define MAXGAMEMOVES 2048

enum { EMPTY, rP, rN, rB, rR, rQ, rK, bP, bN, bB, bR, bQ, bK, yP, yN, yB, yR, yQ, yK, gP, gN, gB, gR, gQ, gK };

enum { FILE_A, FILE_B, FILE_C, FILE_D, FILE_E, FILE_F, FILE_G, FILE_H, FILE_I, FILE_J, FILE_K, FILE_L, FILE_M, FILE_N, FILE_NONE };
enum { RANK_1, RANK_2, RANK_3, RANK_4, RANK_5, RANK_6, RANK_7, RANK_8, RANK_9, RANK_10, RANK_11, RANK_12, RANK_13, RANK_14, RANK_NONE };

enum { RED, BLUE, YELLOW, GREEN, ALL };
enum { RY, BG, BOTH };

enum { RKCA = 1, RQCA = 2, BKCA = 3, BQCA = 4, YKCA = 5, YQCA = 6, GKCA = 7, GQCA = 8 };

enum {
    A1 = 33,  B1, C1, D1, E1, F1, G1, H1, I1, J1, K1, L1, M1, N1,
    A2 = 49,  B2, C2, D2, E2, F2, G2, H2, I2, J2, K2, L2, M2, N2,
    A3 = 65,  B3, C3, D3, E3, F3, G3, H3, I3, J3, K3, L3, M3, N3,
    A4 = 81,  B4, C4, D4, E4, F4, G4, H4, I4, J4, K4, L4, M4, N4,
    A5 = 97,  B5, C5, D5, E5, F5, G5, H5, I5, J5, K5, L5, M5, N5,
    A6 = 113,  B6, C6, D6, E6, F6, G6, H6, I6, J6, K6, L6, M6, N6,
    A7 = 129,  B7, C7, D7, E7, F7, G7, H7, I7, J7, K7, L7, M7, N7,
    A8 = 145,  B8, C8, D8, E8, F8, G8, H8, I8, J8, K8, L8, M8, N8,
    A9 = 161,  B9, C9, D9, E9, F9, G9, H9, I9, J9, K9, L9, M9, N9,
    A10 = 177,  B10, C10, D10, E10, F10, G10, H10, I10, J10, K10, L10, M10, N10,
    A11 = 193,  B11, C11, D11, E11, F11, G11, H11, I11, J11, K11, L11, M11, N11,
    A12 = 209,  B12, C12, D12, E12, F12, G12, H12, I12, J12, K12, L12, M12, N12,
    A13 = 225,  B13, C13, D13, E13, F13, G13, H13, I13, J13, K13, L13, M13, N13,
    A14 = 241,  B14, C14, D14, E14, F14, G14, H14, I14, J14, K14, L14, M14, N14, NO_SQ
};

enum { FALSE, TRUE };

typedef struct {

    int move;
    int castlePerm;
    int enPas;
    int fiftyMove;
    U160 posKey;

} S_UNDO;

typedef struct {

    int pieces[BRD_SQ_NUM];
    U160 pawns[5];

    int KingSq[4];

    int color;
    int enPas;
    int fiftyMove;

    int ply;
    int hisPly;

    U160 posKey;

    int pceNum[25];
    
    int bigPce[5];
    int majPce[5];
    int minPce[5];

    S_UNDO history[MAXGAMEMOVES];

} S_BOARD;

#endif