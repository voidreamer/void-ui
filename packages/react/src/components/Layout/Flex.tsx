import { forwardRef, type HTMLAttributes, type ReactNode } from 'react'
import { cn } from '../../utils'

export interface FlexProps extends HTMLAttributes<HTMLDivElement> {
  /** Flex direction */
  direction?: 'row' | 'column'
  /** Center both axes */
  center?: boolean
  /** Space between */
  between?: boolean
  /** Align items center */
  alignCenter?: boolean
  /** Gap size */
  gap?: 'xs' | 'sm' | 'md' | 'lg'
  children?: ReactNode
}

export const Flex = forwardRef<HTMLDivElement, FlexProps>(
  ({ direction, center, between, alignCenter, gap, className, children, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        'void-flex',
        direction === 'column' && 'void-flex-col',
        center && 'void-flex-center',
        between && 'void-flex-between',
        alignCenter && 'void-flex-align',
        gap && `void-gap-${gap}`,
        className,
      )}
      {...props}
    >
      {children}
    </div>
  )
)

Flex.displayName = 'Flex'
