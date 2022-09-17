rule _TaiShanXiangYu_LockSoft_DLL_V1_0__zlocksoft__Sign_By_fly_qbtxnn
{
	meta:
		description = "TaiShanXiangYu LockSoft DLL V1_0 __ zlocksoft _ Sign_By_fly"
	strings:
		$a = {60E8000000005D81EDE30042008BD581C23201420052E801000000C3C3E803000000EB01??E80E000000E8D1FFFFFFC3E803000000EB01??33C064FF30648920CCC3E803000000EB01??33C064FF306489204BCCC3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
