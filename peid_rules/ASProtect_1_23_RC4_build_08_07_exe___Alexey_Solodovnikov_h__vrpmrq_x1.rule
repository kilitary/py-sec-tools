rule _ASProtect_1_23_RC4_build_08_07_exe___Alexey_Solodovnikov_h__vrpmrq
{
	meta:
		description = "ASProtect 1_23 RC4 build 08_07 _exe_ __ Alexey Solodovnikov _h_"
	strings:
		$a = {9060E803000000E9EB045D4555C3E801000000EB5DBBEDFFFFFF03DD81EB????????807D4D01750C8B74242883FE01895D4E75318D45535053FFB5D50900008D453550E98200000000000000000000000000000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
