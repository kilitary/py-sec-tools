rule _PocketPC_ARM_wwddog
{
	meta:
		description = "PocketPC ARM"
	strings:
		$a = {0305401AB8????8CCA03D08CC981C1????51B9????510606B1??518CD3}
	condition:
		$a in (entrypoint..entrypoint + 11111110)
}
