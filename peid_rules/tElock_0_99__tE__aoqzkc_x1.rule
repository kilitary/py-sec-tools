rule _tElock_0_99__tE__aoqzkc
{
	meta:
		description = "tElock 0_99 __ tE_"
	strings:
		$a = {E95EDFFFFF000000????????E5????00000000000000000005}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
