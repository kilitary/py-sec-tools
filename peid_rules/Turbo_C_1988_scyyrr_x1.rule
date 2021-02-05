rule _Turbo_C_1988_scyyrr
{
	meta:
		description = "Turbo C 1988"
	strings:
		$a = {8CD8BB????8EDB8CD38BCCFA8E??????BC}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
