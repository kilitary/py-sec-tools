rule _with_added_PK_signature_dnkkrf
{
	meta:
		description = "with added _PK_ signature"
	strings:
		$a = {C7??????????8CD805}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
