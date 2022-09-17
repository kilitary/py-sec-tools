rule _CodeSafe_v2_0_fkbvqz
{
	meta:
		description = "CodeSafe v2_0"
	strings:
		$a = {9CFE03??60BE????41??8DBE??10FFFF5783CDFFEB10}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
