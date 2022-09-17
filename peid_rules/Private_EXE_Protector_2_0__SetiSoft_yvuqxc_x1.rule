rule _Private_EXE_Protector_2_0__SetiSoft_yvuqxc
{
	meta:
		description = "Private EXE Protector 2_0 __ SetiSoft"
	strings:
		$a = {89????380000008B??0000000081??????????89??0000000081??0400000081??0400000081??000000000F85D6FFFFFF}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
