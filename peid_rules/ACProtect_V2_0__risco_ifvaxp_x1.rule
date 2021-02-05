rule _ACProtect_V2_0__risco_ifvaxp
{
	meta:
		description = "ACProtect V2_0 __ risco"
	strings:
		$a = {68????????68????????C3C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
