rule _Excalibur_1_03__forgot_mpcrcz
{
	meta:
		description = "Excalibur 1_03 __ forgot"
	strings:
		$a = {E90000000060E8000000005883C008}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
