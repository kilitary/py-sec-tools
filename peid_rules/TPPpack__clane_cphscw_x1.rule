rule _TPPpack__clane_cphscw
{
	meta:
		description = "TPPpack __ clane"
	strings:
		$a = {E8000000005D81EDF58F40006033??E8}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
