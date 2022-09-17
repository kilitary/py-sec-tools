rule __NET_executable_lifyqx
{
	meta:
		description = "_NET executable"
	strings:
		$a = {FF15FC814000B12238087402B120408038007410}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
