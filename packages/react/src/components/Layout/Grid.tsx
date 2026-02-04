import { forwardRef, type HTMLAttributes, type ReactNode } from 'react'
import { cn } from '../../utils'

export interface GridProps extends HTMLAttributes<HTMLDivElement> {
  /** Number of columns */
  cols?: 2 | 3 | 'auto'
  children?: ReactNode
}

export const Grid = forwardRef<HTMLDivElement, GridProps>(
  ({ cols = 'auto', className, children, ...props }, ref) => (
    <div
      ref={ref}
      className={cn(
        'void-grid',
        typeof cols === 'number' ? `void-grid-${cols}` : 'void-grid-auto',
        className,
      )}
      {...props}
    >
      {children}
    </div>
  )
)

Grid.displayName = 'Grid'
