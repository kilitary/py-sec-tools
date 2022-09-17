rule _Borland_C__1991_sodfab
{
	meta:
		description = "Borland C__ 1991"
	strings:
		$a = {2E8C06????2E8C1E????BB????8EDB1EE8????1F}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
