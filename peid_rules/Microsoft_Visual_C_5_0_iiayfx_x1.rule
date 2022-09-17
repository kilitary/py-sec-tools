rule _Microsoft_Visual_C_5_0_iiayfx
{
	meta:
		description = "Microsoft Visual C 5_0"
	strings:
		$a = {64A100000000506489250000000083C4A8535657}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
