rule _ANDpakk2_0_06__Dmitry_Andreev_aifemh
{
	meta:
		description = "ANDpakk2 0_06 __ Dmitry Andreev"
	strings:
		$a = {60FCBED4004000BF001000015783CDFF33C9F9EB05A402DB75058A1E4612DB72F433C04002DB75058A1E4612DB13C002DB75058A1E4612DB720E}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
