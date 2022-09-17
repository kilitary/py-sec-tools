rule _EXE32Pack_v1_39_lkwroj
{
	meta:
		description = "EXE32Pack v1_39"
	strings:
		$a = {8BECFAC7????????4C4CC3FBBF????B8????2E????D1C84F81}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
