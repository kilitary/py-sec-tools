rule _FreeHand_8_document_kmwksp
{
	meta:
		description = "FreeHand 8 document"
	strings:
		$a = {41474433}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
