rule _Exact_Audio_Copy_orjiuu
{
	meta:
		description = "Exact Audio Copy"
	strings:
		$a = {E8??????0031ED5589E581EC??0000008DBD??FFFFFFB9??000000}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
