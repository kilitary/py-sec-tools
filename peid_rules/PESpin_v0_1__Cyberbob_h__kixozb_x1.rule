rule _PESpin_v0_1__Cyberbob_h__kixozb
{
	meta:
		description = "PESpin v0_1 __ Cyberbob _h_"
	strings:
		$a = {EB01??60E8000000008B1C2483C312812BE8B10600FE4BFD822C2488DF46000BE4749E7501C7817304D77AF72F817319770043B7F6C36BB70000F9FFE3C9C208}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
