rule _PEMangle_dozwfg
{
	meta:
		description = "PEMangle"
	strings:
		$a = {609CBE????????8BFEB9????????BB44524F4CAD33C3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
