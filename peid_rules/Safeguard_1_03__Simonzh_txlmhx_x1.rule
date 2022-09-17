rule _Safeguard_1_03__Simonzh_txlmhx
{
	meta:
		description = "Safeguard 1_03 __ Simonzh"
	strings:
		$a = {E8??000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
