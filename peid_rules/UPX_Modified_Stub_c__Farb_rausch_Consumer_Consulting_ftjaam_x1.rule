rule _UPX_Modified_Stub_c__Farb_rausch_Consumer_Consulting_ftjaam
{
	meta:
		description = "UPX Modified Stub c __ Farb_rausch Consumer Consulting"
	strings:
		$a = {60BE????????8DBE????????5783CDFFFCB280E8000000005B83C366A4FFD373FB31C9FFD3731431C0FFD3731D41B010FFD310C073FA753CAAEBE2E84A00000049E210E840000000EB28ACD1E8744511C9EB1C9148}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
