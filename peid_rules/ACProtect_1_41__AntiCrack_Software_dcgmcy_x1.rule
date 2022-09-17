rule _ACProtect_1_41__AntiCrack_Software_dcgmcy
{
	meta:
		description = "ACProtect 1_41 __ AntiCrack Software"
	strings:
		$a = {E801000000??83}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
