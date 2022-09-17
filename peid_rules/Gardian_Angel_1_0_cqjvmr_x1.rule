rule _Gardian_Angel_1_0_cqjvmr
{
	meta:
		description = "Gardian Angel 1_0"
	strings:
		$a = {068CC88ED88EC0FCBF????EB}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
